#Task 2
!pip install pgmpy
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([
    ('Intelligence', 'Grade'),
    ('StudyHours', 'Grade'),
    ('Difficulty', 'Grade'),
    ('Grade', 'Pass')
])

cpd_i = TabularCPD('Intelligence', 2, [[0.7], [0.3]])  
cpd_s = TabularCPD('StudyHours', 2, [[0.6], [0.4]])   
cpd_d = TabularCPD('Difficulty', 2, [[0.4], [0.6]])  
cpd_g = TabularCPD(
    variable='Grade',
    variable_card=3,
    values=[
        [0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9],  
        [0.5,0.4,0.4,0.3,0.3,0.2,0.1,0.05], 
        [0.3,0.3,0.2,0.2,0.1,0.1,0.1,0.05]  
    ],
    evidence=['Intelligence','StudyHours','Difficulty'],
    evidence_card=[2,2,2]
)
cpd_p = TabularCPD(
    variable='Pass',
    variable_card=2,
    values=[
        [0.05, 0.2, 0.5],  
        [0.95, 0.8, 0.5]   
    ],
    evidence=['Grade'],
    evidence_card=[3]
)
model.add_cpds(cpd_i, cpd_s, cpd_d, cpd_g, cpd_p)
assert model.check_model()
infer = VariableElimination(model)
q1 = infer.query(variables=['Pass'],
                 evidence={'StudyHours':0, 'Difficulty':0}) 
print(q1)

q2 = infer.query(variables=['Intelligence'],
                 evidence={'Pass':1})
print(q2)
