// 主命名空间 - 使用与噪音相关的颜色和图标
//% color="#FF5722" icon="\uf130" block="噪音分贝转换"
//% version="1.0.0"
namespace noiseDbConverter {

    /**
     * 将模拟值转换为分贝(dB)值
     * 使用公式: dB = 20 * log10((adcValue / 4095 * 3.3 + 0.001) / 0.00631)
     * @param adcValue 模拟值 (0-4095)
     */
    //% block="将模拟值 [adcValue] 转换为分贝"
    //% adcValue.shadow="number" adcValue.defl=2048
    //% blockType="reporter"
    //% weight=100
    export function convertToDecibel(parameter: any, block: any): void {
        let adcValue = parameter.adcValue.code;

        // 添加必要的头文件
        Generator.addInclude('math.h', '#include <math.h>');
        
        // 生成转换代码
        Generator.addCode(`(20.0 * log10((${adcValue} / 4095.0 * 3.3 + 0.001) / 0.00631))`);
    }
}
