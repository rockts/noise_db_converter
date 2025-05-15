// 声明Generator接口，这是必需的，用于让TypeScript理解Generator对象
declare interface Generator {
    addImport(code: string): void;
    addCode(code: string): void;
    addObject(key: string, value: string): void;
}
declare const Generator: Generator;

// 主命名空间 - 使用与噪音相关的颜色和图标
//% color="#FF5722" icon="\uf130" block="噪音分贝转换"
//% version="1.0.0"
namespace noiseDbConverter {

    /**
     * 将模拟值转换为分贝(dB)值
     * 使用公式: voltage = adc_value / 4095 * 3.3
     *          dB = 20 * log10((voltage + 0.001) / 0.00631)
     * @param adcValue 模拟值 (0-4095)
     */
    //% block="将模拟值 [adcValue] 转换为分贝"
    //% adcValue.shadow="number" adcValue.defl=2048
    //% weight=100
    //% blockId=convertToDecibel
    //% blockType="reporter"
    export function convertToDecibel(parameter: any): number {
        let adcValue = parameter.adcValue.code;

        // 导入噪音转换库
        Generator.addImport(`from noise_converter import convert_to_decibel`);

        // 生成转换代码 - 确保正确返回函数结果
        Generator.addCode(`convert_to_decibel(${adcValue})`);

        // 这个返回值在实际运行中不会使用，只是为了满足TypeScript的类型检查
        return 0;
    }
}
