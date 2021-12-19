cmds = [
    "python run_evaluate.py --evaluate checkpoint/poseaug/videopose/gt/2021-07-05T10:32:17.188567_poseaug/ckpt_best_h36m_p1.pth.tar --posenet_name videopose",
    "python run_evaluate.py --posenet_name gcn --evaluate checkpoint/poseaug/gcn/gt/2021-07-02T22:03:59.344319_poseaug/ckpt_best_h36m_p1.pth.tar",
    "python run_evaluate.py --posenet_name stgcn --evaluate checkpoint/poseaug/stgcn/gt/2021-07-05T10:33:01.468542_poseaug/ckpt_best_h36m_p1.pth.tar",
    "python run_evaluate.py --posenet_name mlp --evaluate checkpoint/poseaug/mlp/gt/2021-07-05T10:32:52.995869_poseaug/ckpt_best_h36m_p1.pth.tar",

]

import os
log = open("train_log.log", "a+")
for cmd in cmds:
    log.write(cmd)
    log.write("\n")
    os.system(cmd)