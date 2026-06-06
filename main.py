#!/bin/bash
# ============================================================
#  Markirovka Tizimi — Android APK yasash skripti
#  Talab: Ubuntu 20.04+ yoki WSL2 (Windows Subsystem for Linux)
# ============================================================

set -e
echo "============================================"
echo "  Markirovka Tizimi — Android APK yasash"
echo "============================================"
echo ""

# 1. Tizim paketlari
echo "[1/4] Tizim paketlari o'rnatilmoqda..."
sudo apt-get update -qq
sudo apt-get install -y -qq \
    python3 python3-pip python3-venv \
    git zip unzip openjdk-17-jdk \
    libffi-dev libssl-dev \
    autoconf libtool pkg-config \
    zlib1g-dev libncurses5-dev \
    cmake libltdl-dev \
    > /dev/null 2>&1
echo "[OK] Tizim paketlari tayyor"

# 2. Python muhiti
echo ""
echo "[2/4] Python virtual muhit tayyorlanmoqda..."
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip -q
pip install buildozer cython -q
echo "[OK] Python muhit tayyor"

# 3. APK build
echo ""
echo "[3/4] APK yaratilmoqda (10-30 daqiqa, birinchi marta)..."
echo "      (Keyingi marta ancha tez bo'ladi)"
echo ""
buildozer android debug

# 4. Natija
echo ""
if ls bin/*.apk 1>/dev/null 2>&1; then
    APK=$(ls bin/*.apk | head -1)
    SIZE=$(du -sh "$APK" | cut -f1)
    echo "============================================"
    echo "  TAYYOR!"
    echo "  APK: $APK"
    echo "  Hajmi: $SIZE"
    echo "============================================"
else
    echo "[XATO] APK topilmadi — log ni tekshiring"
    exit 1
fi
