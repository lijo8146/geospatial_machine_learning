import unittest
import numpy as np
from course import points,embeddings,evaluate,h3_summary
class CourseTests(unittest.TestCase):
    def test_group_holdout(self):
        f=points();x=embeddings(f)
        _,metrics,_,train,test=evaluate(f,x)
        self.assertFalse(set(f.iloc[train].block)&set(f.iloc[test].block))
        self.assertEqual(len(train)+len(test),len(f))
        self.assertTrue(0<=metrics['balanced_accuracy']<=1)
    def test_reject_missing_vectors(self):
        f=points();x=embeddings(f);x[0,0]=np.nan
        with self.assertRaises(ValueError):evaluate(f,x)
    def test_reject_duplicate_ids(self):
        f=points();f.loc[1,'point_id']=f.loc[0,'point_id']
        with self.assertRaises(ValueError):evaluate(f,embeddings(f))
    def test_h3_preserves_mass(self):
        f=points();f['probability']=np.linspace(0,1,len(f))
        for resolution in [6,9]:
            s=h3_summary(f,resolution)
            self.assertEqual(s['count'].sum(),len(f))
            self.assertAlmostEqual(np.average(s.mean_probability,weights=s['count']),f.probability.mean())
if __name__=='__main__':unittest.main()
