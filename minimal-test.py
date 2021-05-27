#! /usr/bin/env python3

import mle
import cressieread
import pdiscressieread

est = mle.Estimator()
megaest = mle.Estimator(wmax=60)
crest = cressieread.Estimator()
crmegaest = cressieread.Estimator(wmax=60)
crint = cressieread.Interval(wmax=60)
crmegaint = cressieread.Interval()
crultraint = cressieread.Interval(wmax=1000000)
pdiscrest = pdiscressieread.Estimator()
pdiscrint = pdiscressieread.Interval()

#for x in [(10, 2, 0)]:

#for x in  [(5532, 0, 0), (2936, 2, 0), (1528, 2, 1), (10, 1000, 1)]:

for x in [ (41332, 0.0, 0.0), (1958, 0.0, 1.0), (17763, 1.0, 0.0), 
           (1339, 1.0, 1.0), (30726, 1.0344828, 0.0), (3867, 1.0344828, 1.0), 
           (2034, 1.0447762, 1.0), (16728, 1.0447762, 0.0), 
           (40629, 1.0497237, 0.0), (3445, 1.0497237, 1.0), 
           (85, 59.999996, 0.0), (6, 59.999996, 1.0) ]:
    est.add_example(p_log=1.0, p_pred=x[1], r=x[2], count=x[0])
    megaest.add_example(p_log=1.0, p_pred=x[1], r=x[2], count=x[0])
    crest.add_example(p_log=1.0, p_pred=x[1], r=x[2], count=x[0])
    crmegaest.add_example(p_log=1.0, p_pred=x[1], r=x[2], count=x[0])
    crint.add_example(p_log=1.0, p_pred=x[1], r=x[2], count=x[0])
    crmegaint.add_example(p_log=1.0, p_pred=x[1], r=x[2], count=x[0])
    crultraint.add_example(p_log=1.0, p_pred=x[1], r=x[2], count=x[0])
    pdiscrest.add_example(p_logs=[1.0]*2, p_preds=[x[1]]*2, rs=[x[2]]*2, count=x[0])
    pdiscrint.add_example(p_logs=[1.0]*2, p_preds=[x[1]]*2, rs=[x[2]]*2, count=x[0])

#print(est.get_estimate())
#print(megaest.get_estimate())
#print(crest.get_estimate())
#print(crmegaest.get_estimate())
print(pdiscrest.get_estimate())
print(crint.get_interval())
print(crmegaint.get_interval())
print(crultraint.get_interval())
print(pdiscrint.get_interval())
