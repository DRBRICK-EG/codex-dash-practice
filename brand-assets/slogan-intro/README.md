# DR.BRICK · 3 秒口号片头

口号：**دكتور بريك… فرحة بإيدك!**  
中文意译：**DR.BRICK，快乐亲手拼！**

- [直接打开 MP4](https://raw.githubusercontent.com/DRBRICK-EG/codex-dash-practice/drbrick-brand-character/brand-assets/slogan-intro/drbrick-slogan-intro-3s.mp4)
- [独立人声 WAV](https://raw.githubusercontent.com/DRBRICK-EG/codex-dash-practice/drbrick-brand-character/brand-assets/slogan-intro/drbrick-slogan-voice.wav)
- [预览图](preview.jpg)

采用已有无胡子卡通品牌人物和原版透明背景 logo。人物轻微摆动，嘴部随人声音量开合，字幕分句出现，配以轻微提示音。属于二维人物动画；嘴部动作由音量驱动，并非逐音素口型匹配。

声音为本地 Piper / Sherpa-ONNX `ar_JO-kareem-medium` 阿拉伯语合成男声，不是本人声线克隆，也未模拟本人的声音。模型语言标签为约旦阿拉伯语；不将其标注为经母语者审校的埃及口音录音。

输出：1080 × 1920，9:16，3.000 秒，30 fps；H.264 Constrained Baseline，yuv420p；AAC-LC，48 kHz 双声道；MP4 faststart。独立 WAV 为不带提示音的人声，可用于后续剪辑。

把 MP4 放在后续产品视频的最前面即可；本片头没有绑定某一款具体产品。

语音模型来源：https://github.com/k2-fsa/sherpa-onnx/releases/tag/tts-models  
模型卡指向的训练数据：https://github.com/AliMokhammad/arabicttstrain/

验证结果：全片解码无报错；Chromium 浏览器起播、跳转和播放至结尾正常。未在实体 Windows 设备上实测。

## V2 · 卡通男孩风格调音试听

- [V2 视频](https://raw.githubusercontent.com/DRBRICK-EG/codex-dash-practice/drbrick-brand-character/brand-assets/slogan-intro/drbrick-slogan-boy-intro-3s-v2.mp4)
- [V2 独立人声](https://raw.githubusercontent.com/DRBRICK-EG/codex-dash-practice/drbrick-brand-character/brand-assets/slogan-intro/drbrick-slogan-boy-voice-v2.wav)

根据“更偏卡通小男孩，减少机械感”的反馈重新分句合成，并调整停顿、动态音高、共振峰和音色，口型重新跟随新版人声。画面与原版 logo 延续第一版，总时长仍为 3 秒。

这是一版基于同一阿拉伯语成人合成模型制作的卡通风格调音试听，未声称采用新的儿童声库或真人儿童录音；实际自然度与情绪表现需试听确认。保留第一版，便于比较。
