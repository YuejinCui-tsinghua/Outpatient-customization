# 智能问诊定制

你好，一线的医生。

你是否厌倦了每天问患者重复的问题？书写重复的病例？

你是否希望每天只开药收钱，早日实现财富自由！

那么赶快定专属问诊软件，重复工作可以让患者扫码完成。

Mchat算法可以从你的以往症状记录，自动学习你的临床经验。

全自动定制软件，无需电子病历上传，保障隐私安全，永久免费！


基于对抗神经网络的辅助智能问诊系统

  医生与患者之间的沟通成本是目前医疗的主要成本。在诊疗之前，患者通常只能描述自身的少量症状。因此医生需要跟患者多轮对话，引导并获取患者主要症状细节。医生通常会将这些症状记录在电子病例的现病史，作为有诊断意义的症状证据。本对抗求证问诊软件，可对话患者自动给医生呈现所需要的症状证据。这样医生不需要进行低效率低价值的沟通工作，专注于高价值的医疗决策。实验表明该算法大部分问题是直接关系到患者疾病的问题。对话后病例的诊断准确率接近专业医生。生成病例和医生标注病例高度相似。

![image](im/chat.png)

如图所示，与患者沟通流程介绍。首先，患者的主诉包含一些简单的症状（e.g.,发烧），作为初始的确认症状。判别器可以实时给出患者可能的疾病，但初期患者症状较少，疾病分类的置信率较低。在对话界面，生成器会根据患者已确认症状，推荐患者可能的症状（e.g.,头痛）以及检查项（e.g.,血常规）。患者可以根据自身情况进行输入调整。经过不断迭代沟通，当判别器认可确认症状是全面症状，会将这些症状生成病例，作为解释给医生的症状证据。同时，医生还可以得到置信率较高的确诊分类。

如果你想定制一个这样的系统，请使用extract.py从病例记录中采集你的临床经验，并发送至邮箱cuiyj17@mails.tsinghua.edu.cn，我们会回复一个小程序二维码。

![image](im/WX.jpg)


