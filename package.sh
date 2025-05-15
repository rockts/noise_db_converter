#!/bin/bash

# Mind+自定义积木打包脚本
# 作者：Your Name
# 日期：2025-05-16

# 获取配置信息
NAME=$(grep -o '"id": *"[^"]*"' config.json | cut -d'"' -f4)
VERSION=$(grep -o '"version": *"[^"]*"' config.json | head -1 | cut -d'"' -f4)
AUTHOR=$(grep -o '"author": *"[^"]*"' config.json | cut -d'"' -f4)
OUTPUT_FILE="${AUTHOR}-${NAME}-thirdex-V${VERSION}.mpext"

# 颜色定义
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${YELLOW}正在打包 Mind+ 自定义积木...${NC}"
echo "名称: $NAME"
echo "版本: $VERSION"
echo "作者: $AUTHOR"
echo "输出文件: $OUTPUT_FILE"

# 创建临时目录
TEMP_DIR="temp_package"
rm -rf "$TEMP_DIR"
mkdir -p "$TEMP_DIR"

echo -e "\n${YELLOW}正在准备文件...${NC}"

# 打包Arduino库文件
if [ -d "arduinoC/libraries" ]; then
    echo "打包Arduino库..."
    cd arduinoC/libraries
    zip -r libraries.zip *.h *.cpp >/dev/null 2>&1
    cd ../..
fi

# 打包Python库文件
if [ -d "python/libraries" ]; then
    echo "打包Python库..."
    cd python/libraries
    zip -r libraries.zip *.py >/dev/null 2>&1
    cd ../..
fi

# 复制文件到临时目录
echo "复制文件到临时目录..."
cp -r config.json "$TEMP_DIR/"
cp -r arduinoC "$TEMP_DIR/"
cp -r python "$TEMP_DIR/"

# 删除不必要的文件
find "$TEMP_DIR" -name ".DS_Store" -delete
find "$TEMP_DIR" -name "*.git*" -delete

# 打包成mpext文件
echo -e "\n${YELLOW}创建最终扩展包...${NC}"
cd "$TEMP_DIR"
zip -r "../$OUTPUT_FILE" * >/dev/null 2>&1
cd ..

# 清理临时文件
rm -rf "$TEMP_DIR"

# 检查打包结果
if [ -f "$OUTPUT_FILE" ]; then
    FILE_SIZE=$(du -h "$OUTPUT_FILE" | cut -f1)
    echo -e "${GREEN}打包成功！${NC}"
    echo "文件: $OUTPUT_FILE"
    echo "大小: $FILE_SIZE"
    echo -e "\n${YELLOW}提示：${NC}通过Mind+的"扩展"->"管理扩展"->"本地导入"导入此文件"
else
    echo -e "${RED}打包失败！${NC}"
fi