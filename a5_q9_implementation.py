import random
import viterbi_a5_q9
import figures
from copy import deepcopy

# Global variables: list of possible symptoms, states, and start probabilities
possible_symptoms = ['nausea', 'vomiting', 'coughing', 'fever', 'chills', 'sore throat', 'diarrhea', 'stuffy nose', 'aches']
states = ('sick', 'healthy')
start_prob = {'sick' : 1.0, 'healthy' : 0.0}

# Generates problem and prints it in Python terminal
def generate_problem():
    # Generate symptom list for problem
    problem_symptoms = generate_symptoms() # unique list of symptoms for each generated problem
    state_diagram_path = generate_figure(problem_symptoms) # returns string of path to blank state diagram
    sick_appears_healthy = random.randint(10, 20) # sick patients appear healthy sick_sppears_healthy precent of the time
    healthy_appears_sick = random.randint(20, 40) # healthy patients appear sick healthy_appears_sick percent of the time
    recovery_chance = random.randint(2, 5) # patient has a 1 in recovery_chance probability of becoming healthy each day
    observations = generate_observations(problem_symptoms) # unique list of observations for each generated problem
    T = generate_tMatrix(recovery_chance) # Transition matrix
    E = generate_eMatrix(problem_symptoms, sick_appears_healthy, healthy_appears_sick) # Emission matrix
    V = viterbi_a5_q9.viterbi(observations, states, start_prob, T, E) # returns list of most likely states
    # Prints probelm statements
    print_problem(problem_symptoms, sick_appears_healthy, healthy_appears_sick, recovery_chance, observations, state_diagram_path)
    # Prints solutions to generated problem
    generate_solutions(problem_symptoms, sick_appears_healthy, healthy_appears_sick, recovery_chance, observations, V)

# Generates solutions and prints them in Python terminal
def generate_solutions(PS, SAH, HAS, RC, Obs, V):
    # Labels for states
    state_labels = deepcopy(states)
    # Labels for possible emitted symbols
    emission_labels = deepcopy(PS)
    # Probability of state transition from sick to healthy
    sick_to_healthy_prob = 1/deepcopy(RC)
    # Probability of state transition from healthy to sick
    healthy_to_sick_prob = (deepcopy(RC)-1)/deepcopy(RC) 
    # Probability labels for emission arrows from healthy state to any symptom
    healthy_to_symptom_prob = deepcopy(HAS)/(len(PS))/100
    # Probability labels for emission arrow from healthy state to symptom free
    healthy_to_symptomFree_prob = 1-len(PS)*healthy_to_symptom_prob
    # Probability labels for emission arrows from sick state to any symptom
    sick_to_symptom_prob = (100-deepcopy(SAH))/(len(PS))/100
    # Probability labels for emission arrows from sick state to symptom free
    sick_to_syptomFree_prob = deepcopy(SAH)/100
    min_recover_days = find_healthy(deepcopy(V))
    emission_labels.append('symptom free')
    print_solutions(state_labels, emission_labels, sick_to_healthy_prob, healthy_to_sick_prob, 
                    healthy_to_symptom_prob, healthy_to_symptomFree_prob, 
                    sick_to_symptom_prob, sick_to_syptomFree_prob, min_recover_days)
    print_CorrectStudentInputAnswers(state_labels, emission_labels, sick_to_healthy_prob, healthy_to_sick_prob, 
                    healthy_to_symptom_prob, healthy_to_symptomFree_prob, 
                    sick_to_symptom_prob, sick_to_syptomFree_prob, min_recover_days)

# Prints the problem in python terminal
def print_problem(Symp, SAH, HAS, RC, Obs, ImgPath):
    Symp.remove('symptom free')
    sympString = list_to_string(Symp)
    obsString = list_to_string(Obs)
    print('\n \nWe are going to perform a study to determine the recovery time of sick patients.'
    + ' Each day we monitor the patient, we will record their most serious symptom out of', sympString,
    'If the patient does not display any of these behaviours, we can record that they were symptom free on that day. '
    + 'Based on previous research, these symptoms are all equally as likely to appear in someone who is sick, and collectively only appear',
    HAS, '%' + ' of the time in healthy individuals, each with equal probability, and otherwise a healthy individual is symptom free.' 
    + ' Furthermore, sick patients are known to be symptom free', SAH, '%' + ' of the time. Lastly, sick patients have a 1 in',
    RC, 'chance of recovering on any given day, and healthy patients have a',
    RC-1, 'in', RC, 'chance of becoming sick again. Assume all patients are sick at the start of the monitoring period. \n \n'
    + '     a) Label the state diagram below to represent this problem. See', ImgPath, 'for the blank state diagram.'
    + ' Label the diagram from left to right in the order that variables appear in the problem statement. \n'
    + '     b) We monitored a patient over', len(Obs), 'days and recorded the symptoms:', obsString,
    'What is the least number of days after which they may have been suspected to recover? Enter 0 if they did not recover.\n \n')

# Prints solutions
def print_solutions(SL, EL, SHP, HSP, HESP, HEHP, SESP, SEHP, MRD):
    print('\n Solutions to the randomly generated problem: ')
    print('\n \n State labels:', SL)
    print('\n Emitted symbol labels:', EL)
    print('\n Sick state to healthy state transition probability:', SHP)
    print('\n Sick state to sick state transition probability:', 1-SHP)
    print('\n Healthy state to sick state transition probability:', HSP)
    print('\n Healthy state to healthy state transition probability:', 1-HSP)
    print('\n Sick state to emit symptom probability:', SESP)
    print('\n Sick state to emit symptom free probabilty:', SEHP)
    print('\n Healthy state to emit any symptom probability:', HESP)
    print('\n Healthy state to emit symptom free probability:', HEHP)
    print('\n Minumum number of days before patient may have recoverd', MRD)
    print('\n \n')

# Prints what the student should have inputted 
def print_CorrectStudentInputAnswers(SL, EL, SHP, HSP, HESP, HEHP, SESP, SEHP, MRD):
    # Multiple choice options
    choices = ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)', '(g)', '(h)', '(i)', '(j)', '(k)', '(l)', '(m)', '(n)', '(o)', '(p)', '(q)', '(r)', '(s)', '(t)', '(u)', '(v)', '(w)', '(x)', '(y)', '(z)'] 
    E = len(EL)-1
    stateChoices = choices[0:2]
    transitionProbChoices = choices[2:6]
    transitionProbs = [SHP, 1-SHP, HSP, 1-HSP]
    emissionChoices = choices[6:7+E]
    sickEmitSymptomProbChoices = choices[7+E:7+2*E]
    sickEmitHealthyProbChoices = choices[7+2*E:8+2*E]
    healthyEmitSymptomProbChoices = choices[8+2*E:8+3*E]
    healthyEmitHealthyProbChoices = choices[8+3*E:9+3*E]
    print('Student\'s correct input based on corresponding figure: \n')
    for n in range (len(stateChoices)):
        print(stateChoices[n] + ':', SL[n])
    for n in range (len(transitionProbChoices)):
        print(transitionProbChoices[n] +  ':', transitionProbs[n])
    for n in range (len(emissionChoices)):
        print(emissionChoices[n] + ':', EL[n])
    for n in range (len(sickEmitSymptomProbChoices)):
        print(sickEmitSymptomProbChoices[n] + ':', SESP)
    for n in range (len(sickEmitHealthyProbChoices)):
        print(sickEmitHealthyProbChoices[n] + ':', SEHP)
    for n in range (len(healthyEmitSymptomProbChoices)):
        print(healthyEmitSymptomProbChoices[n] + ':', HESP)
    for n in range (len(healthyEmitHealthyProbChoices)):
        print(healthyEmitHealthyProbChoices[n] + ':', HEHP)
    print('Minimum number of days before suspected recovery:', MRD)

# Helper functions:

def generate_symptoms():
    #nSymptoms = random.randint(2, 5)
    nSymptoms = 4
    temp_symptoms = possible_symptoms
    problem_symptoms = []
    for i in range(nSymptoms):
        x = random.randint(0, len(temp_symptoms)-1)
        s = temp_symptoms[x]
        problem_symptoms.append(s)
        temp_symptoms.remove(s)
    return problem_symptoms

def generate_observations(symptoms):
    symptoms.append('symptom free')
    days = random.randint(5, 8)
    observations = []
    for day in range(days):
        o = random.choice(symptoms)
        observations.append(o)
    return observations

# Generates transmission matrix for Viterbi
def generate_tMatrix(recovery_chance):
    recovery_prob = 1/recovery_chance # pateint has a 1 in recovery_chance probability of becoming healthy on a given day
    T = {'sick' : {'sick' : 1-recovery_prob, 'healthy' : recovery_prob},
         'healthy' : {'sick' : 1-recovery_prob, 'healthy' : recovery_prob}
    }
    print(T)
    return T

# Generates emission matrix for Viterbi
def generate_eMatrix(symptoms, sick_appears_healthy, healthy_appears_sick):
    SAH = sick_appears_healthy/100 # express prob of sick patient appearing healthy as decimal
    HAS = healthy_appears_sick/100 # express prob of heatlhy patient appearing sick as decimal
    sick_symptom_prob = (1-SAH)/(len(symptoms)-1) # probability of sick patient displaying any symptom
    healthy_symptom_prob = HAS/(len(symptoms)-1) # probability of healthy patient displaying any symptom
    E = {'sick' : {}, 
         'healthy' : {}
    }
    for s in symptoms:
        E['sick'][s] = sick_symptom_prob
        E['healthy'][s] = healthy_symptom_prob
    E['sick']['symptom free'] = SAH
    E['healthy']['symptom free'] = 1-HAS
    print(E)
    return E

# Picks correct figure for problem variant
def generate_figure(symptoms):
    n = len(symptoms)
    if n == 2:
        return("figures/a5_q9_2symptoms_final.png")
    if n == 3:
        return("figures/a5_q9_3symptoms_final.png")
    if n == 4:
        return("figures/a5_q9_4symptoms_final.png")
    else: 
        return("figres/a5_q9_5symptoms_final.png")

# Finds first occurence of 'healthy' in optimal path, 0 if none exists
def find_healthy(V):
    occ = 1
    for s in V:
        if s == 'healthy':
            return occ
        else:
            occ = occ+1
    return 0
        
# Turns lists to nice strings for printing
def list_to_string(inList):
    lst = deepcopy(inList)
    s = ''
    last = lst[-1]
    lst.remove(last)
    for l in lst:
        s = s + l + ', '
    s = s + 'and ' + last + '.'
    return s

generate_problem()