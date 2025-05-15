# 自定义积木模板使用示例

本文档提供了使用自定义积木模板的示例代码，帮助您了解如何在 Arduino 和行空板上使用这些积木。

## Arduino 示例

### 基础使用示例

下面的 Arduino 代码示例展示了如何使用自定义积木进行基本操作：

```cpp
#include "CustomDevice.h"

// 创建设备对象
CustomDevice customDevice(&Wire);

void setup() {
  // 初始化串口
  Serial.begin(9600);
  Serial.println("自定义设备测试程序");

  // 初始化设备
  if (customDevice.begin()) {
    Serial.println("设备初始化成功！");
  } else {
    Serial.println("设备初始化失败，请检查连接");
    while (1); // 停止程序
  }

  // 设置参数
  customDevice.setParameter(50);
}

void loop() {
  // 读取各类数据
  uint16_t rawData = customDevice.readRawData();
  uint16_t processedData = customDevice.readProcessedData();
  uint8_t statusValue = customDevice.readStatusValue();

  // 打印数据
  Serial.print("原始数据: ");
  Serial.println(rawData);
  Serial.print("处理后数据: ");
  Serial.println(processedData);
  Serial.print("状态值: ");
  Serial.println(statusValue);

  // 每次读取间隔1秒
  delay(1000);

  // 每5次循环执行一次动作
  static int count = 0;
  count++;
  if (count >= 5) {
    Serial.println("执行动作");
    customDevice.performAction();
    count = 0;
  }
}
```

### 高级使用示例

下面的示例展示了更多高级功能和错误处理：

```cpp
#include "CustomDevice.h"

// 取消注释下面一行以开启调试信息
// #define ENABLE_DBG

CustomDevice customDevice(&Wire);

// 定义状态值对应的文本描述
const char* statusText[] = {
  "空闲",
  "忙碌",
  "错误",
  "警告",
  "正常",
  "未知"
};

void setup() {
  Serial.begin(9600);
  Serial.println("自定义设备高级测试");

  // 尝试多次初始化设备
  bool success = false;
  for (int i = 0; i < 3; i++) {
    Serial.print("尝试初始化设备 (");
    Serial.print(i + 1);
    Serial.print("/3)... ");

    if (customDevice.begin()) {
      Serial.println("成功！");
      success = true;
      break;
    } else {
      Serial.println("失败");
      delay(1000);
    }
  }

  if (!success) {
    Serial.println("设备初始化失败，请检查连接。进入模拟模式。");
    // 继续运行，但使用模拟数据
  }

  // 设置参数
  Serial.println("设置设备参数为75");
  customDevice.setParameter(75);
}

void loop() {
  // 读取数据并进行错误处理
  uint16_t rawData = 0;
  uint16_t processedData = 0;
  uint8_t statusValue = 0;

  // 使用try-catch结构捕获可能的异常
  try {
    rawData = customDevice.readRawData();
    processedData = customDevice.readProcessedData();
    statusValue = customDevice.readStatusValue();

    // 确保状态值在有效范围内
    if (statusValue >= 6) {
      statusValue = 5; // 使用"未知"状态
    }

    // 数据处理和显示
    Serial.println("===== 设备数据 =====");
    Serial.print("原始数据: ");
    Serial.println(rawData);
    Serial.print("处理后数据: ");
    Serial.println(processedData);
    Serial.print("状态值: ");
    Serial.print(statusValue);
    Serial.print(" (");
    Serial.print(statusText[statusValue]);
    Serial.println(")");

    // 根据状态执行不同操作
    if (statusValue == 1) { // 忙碌
      Serial.println("设备忙碌，等待...");
    } else if (statusValue == 2) { // 错误
      Serial.println("检测到错误，重置设备...");
      customDevice.performAction();
    }

  } catch (...) {
    Serial.println("读取数据时发生错误");
  }

  delay(2000);
}
```

## Python/行空板示例

### 基础使用示例

下面的 Python 代码示例展示了如何在行空板上使用自定义设备库：

```python
from custom_device import CustomDevice
import time

# 创建设备对象
device = CustomDevice()

# 初始化设备
print("正在初始化设备...")
if device.begin():
    print("设备初始化成功！")
else:
    print("设备初始化失败，将使用模拟模式")

# 设置参数
device.set_parameter(50)
print("参数设置为50")

# 循环读取数据
try:
    while True:
        # 读取各类数据
        raw_data = device.read_raw_data()
        processed_data = device.read_processed_data()
        status_value = device.read_status_value()

        # 打印数据
        print("原始数据:", raw_data)
        print("处理后数据:", processed_data)
        print("状态值:", status_value)
        print("-" * 20)

        # 每次读取间隔1秒
        time.sleep(1)

except KeyboardInterrupt:
    print("\n程序已停止")
```

### 高级使用示例

下面的示例展示了更多 Python 高级特性和行空板特定功能：

```python
from custom_device import CustomDevice
import time
import sys

# 定义状态值对应的文本描述
STATUS_TEXT = [
    "空闲",
    "忙碌",
    "错误",
    "警告",
    "正常",
    "未知"
]

# 设置结构化数据显示格式
def print_data(raw, processed, status):
    """格式化打印设备数据"""
    status_desc = STATUS_TEXT[status] if status < len(STATUS_TEXT) else "未知"

    print("┌─────────────────────────┐")
    print(f"│ 设备数据        状态: {status_desc:<5} │")
    print("├─────────────────────────┤")
    print(f"│ 原始数据: {raw:<14} │")
    print(f"│ 处理值:   {processed:<14} │")
    print("└─────────────────────────┘")

# 创建设备对象 - 强制使用真实设备
try:
    print("尝试初始化真实设备...")
    device = CustomDevice(force_real=True)
    success = device.begin()
    if not success:
        print("无法初始化真实设备，程序退出")
        sys.exit(1)
except Exception as e:
    print(f"错误: {e}")
    print("无法初始化设备，程序退出")
    sys.exit(1)

# 设置初始参数
print("设置设备参数...")
device.set_parameter(75)

# 收集历史数据进行简单分析
history = []

# 主循环
print("开始数据收集...")
try:
    count = 0
    while True:
        # 读取数据
        raw = device.read_raw_data()
        processed = device.read_processed_data()
        status = device.read_status_value()

        # 保存历史数据 (最多保存10条)
        history.append(raw)
        if len(history) > 10:
            history.pop(0)

        # 计算简单统计信息
        if history:
            avg = sum(history) / len(history)
            min_val = min(history)
            max_val = max(history)

            # 检测数据变化趋势
            trend = "稳定"
            if len(history) >= 3:
                if history[-1] > history[-2] > history[-3]:
                    trend = "上升"
                elif history[-1] < history[-2] < history[-3]:
                    trend = "下降"

        # 格式化显示数据
        print_data(raw, processed, status)
        if history:
            print(f"统计: 平均={avg:.1f} 最小={min_val} 最大={max_val} 趋势={trend}")

        # 根据状态执行相应操作
        if status == 2:  # 错误状态
            print("检测到错误状态，执行修复操作...")
            device.perform_action()

        # 周期性执行动作
        count += 1
        if count >= 5:
            print("执行周期性动作...")
            device.perform_action()
            count = 0

        time.sleep(2)

except KeyboardInterrupt:
    print("\n程序已停止")
```

## Mind+积木示例

在 Mind+中，可以直接拖拽积木使用。以下是几个常见的使用场景：

### Arduino 平台

1. **基本读取示例**

   - 初始化设备积木
   - 循环中使用"读取原始数据"积木并显示在串口监视器中
   - 每次循环间添加延时积木

2. **监控与执行示例**

   - 初始化设备积木
   - 循环中读取状态值
   - 使用条件积木判断状态值，当状态为特定值时执行动作
   - 在屏幕或 LCD 上显示当前设备状态

### 行空板平台

1. **数据记录示例**

   - 初始化设备积木
   - 循环中读取处理后数据
   - 将数据记录到文件中
   - 绘制实时数据图表

2. **自动控制示例**

   - 初始化设备积木
   - 设置初始参数值
   - 循环中读取数据并根据数据调整参数
   - 当读取值超过阈值时执行设备动作

## 注意事项

1. 确保硬件正确连接，尤其是 I2C 地址的设置
2. Arduino 环境中需要包含 Wire 库
3. 行空板环境已默认包含必要的库文件
4. 模拟模式在没有实际硬件时提供便利，但实际值会与真实设备不同
