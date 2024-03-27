result summary: https://docs.google.com/spreadsheets/d/1c9U8fvE300uHtcBeyIueRFxIoW3LxEWHHXL_1eQ9dao/edit?usp=sharing


Dataset Link: https://archive.ics.uci.edu/dataset/94/spambase

真正例（True Positives, TP）：模型正确预测为正类的样本数量。
假正例（False Positives, FP）：模型错误预测为正类的样本数量。
真负例（True Negatives, TN）：模型正确预测为负类的样本数量。
假负例（False Negatives, FN）：模型错误预测为负类的样本数量。

准确率（Accuracy）
准确率是正确预测的样本（无论正类还是负类）占总样本的比例。例子：如果我们有100封邮件，模型正确地识别出了90封（包括垃圾邮件和非垃圾邮件），则准确率为90%。

精确率（Precision）
精确率是正确预测为正类的样本占所有预测为正类样本的比例。它反映了模型预测正类的准确性。例子：如果模型预测有50封垃圾邮件，但其中只有40封是真正的垃圾邮件（即TP=40），其余10封是错误分类的非垃圾邮件（FP=10），那么精确率为80%。

召回率（Recall）
召回率是正确预测为正类的样本占所有实际正类样本的比例。它反映了模型捕获正类样本的能力。例子：如果实际有60封垃圾邮件，模型只正确识别出了50封（TP=50），另有10封垃圾邮件被误判为非垃圾邮件（FN=10），那么召回率为83.33%。

F1得分（F1 Score）
F1得分是精确率和召回率的调和平均数，用于衡量模型的精确度和健壮性。当精确率和召回率都很重要时，F1得分是一个有用的指标。例子：如果精确率为80%，召回率为83.33%，则F1得分为81.63%。
