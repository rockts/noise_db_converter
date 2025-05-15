# 噪音分贝转换积木

这是一个用于 Mind+的噪音传感器分贝值转换### Arduino 示例代码

````cpp
/### 行空板(Unihiker)示例代码

```python
from pinpong.board import Board, Pin
from noise_converter import convert_to_decibel
import time

# 初始化行空板
Board("unihiker").begin()
p_analog = Pin(Pin.P21, Pin.ANALOG)

# 读取模拟值并转换为分贝
while True:
    analog_value = p_analog.read_analog()
    db_value = convert_to_decibel(analog_value)
    print(f"原始值: {analog_value}, 分贝值: {db_value:.2f} dBA")
    time.sleep(1)
```int rawValue = analogRead(A0);
// Arduino使用10位ADC，需要进行映射
int mappedValue = map(rawValue, 0, 1023, 0, 4095);
// 计算电压值（0-3.3V）
float voltage = mappedValue / 4095.0 * 3.3;
// 使用SEN0232标准公式计算分贝值
float dBA = constrain(voltage * 50.0, 30.0, 130.0);
Serial.print("分贝值: ");
Serial.println(dBA);
```uino (Uno/Mega2560/Leonardo) 和行空板（Unihiker）。此扩展可以将噪音传感器的模拟输出值(0-4095)转换为更加直观的分贝(dB)值。

## 扩展特点

- 🔊 专业转换：使用标准声学公式将模拟值转换为分贝值
- 🧩 简单使用：只需一个积木块即可完成转换
- 🌟 双平台支持：同时支持 Arduino 和行空板平台
- 📚 中英文支持：完整的双语支持

## 转换公式

噪音分贝转换使用DFRobot SEN0232模拟分贝计的标准公式：

````

voltage = adc_value / 4095 _ 3.3
dBA = voltage _ 50

````

其中：

- `adc_value` 是传感器的模拟值 (0-4095)
- `voltage` 是转换后的电压值 (V)
- 返回的 `dBA` 是A计权分贝值，范围在30~130dBA之间

注：当传感器输出电压为0.6V时，对应分贝值为30dBA；当输出电压为2.6V时，对应分贝值为130dBA。

## 使用方法

1. 在 Mind+中导入此扩展
2. 将噪音传感器连接到 Arduino 或行空板的模拟输入端口
3. 使用"将模拟值转换为分贝"积木，传入传感器的模拟读数
4. 得到转换后的分贝值

### Arduino 示例代码

```cpp
// 读取A0模拟输入并转换为分贝值
int rawValue = analogRead(A0);
// Arduino使用10位ADC，需要进行映射
int mappedValue = map(rawValue, 0, 1023, 0, 4095);
float db = 20.0 * log10(((mappedValue / 4095.0 * 3.3) + 0.001) / 0.00631);
Serial.print("分贝值: ");
Serial.println(db);
````

### 行空板(Unihiker)示例代码

```python
from pinpong.board import Board, Pin
from noise_converter import convert_to_decibel
import time

# 初始化行空板
Board("unihiker").begin()
p_analog = Pin(Pin.P21, Pin.ANALOG)

# 读取模拟值并转换为分贝
while True:
    analog_value = p_analog.read_analog()
    db_value = convert_to_decibel(analog_value)
    print(f"原始值: {analog_value}, 分贝值: {db_value:.2f} dB")
    time.sleep(1)
```

## 支持的硬件

- **Arduino**：Uno, Mega2560, Leonardo
- **行空板**：Unihiker

## 许可证

MIT

## 作者

rockts (gaopeng@lekee.cc)
