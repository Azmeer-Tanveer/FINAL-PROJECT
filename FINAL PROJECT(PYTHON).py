print("Welcome to the DISEASE PREDICTOR PROGRAM")
print("This program helps you identify diseases that you may have based on symptoms and affected areas.")

print("\n1: Respiratory  system")
print("2: Muscles")
print("3: Central nervous system")
print("4: Eyes")
print("5: Skin")
print("6: Bloodstream")
print("7: Bladder")
print("8: Kidneys")

choice = input("\nKindly indicate the affected area by the virus (Enter the number corresponding to the affected area): ")

if choice == '1':

    symptoms = input("\nPlease enter your symptoms (separated by commas and in lowercase): ")

    if 'fever' in symptoms or 'cough'in symptoms or 'runny nose'in symptoms:
        print("You may have FLU")
        print("\nCause: The flu is caused by influenza viruses.") 
        print("\nTreatment: It is treated with antiviral medications such as oseltamivir (Tamiflu) to alleviate symptoms and shorten duration.")

    elif ' sneezing' in symptoms or 'sore throat' in symptoms or 'cough'in symptoms :
        print("You may have RHINOVIRUS (COMMON COLD):")
        print("\nCause: The common cold, typically caused by rhinovirus infection") 
        print("\nTreatment: It is managed symptomatically with rest, hydration, and over-the-counter medications like decongestants, antihistamines, and pain relievers.")

    elif 'fever' in symptoms or 'difficulty breathing' in symptoms or 'sore throat' in symptoms:
        print("You may have PARAINFLUENZA VIRUS:")
        print("\nCause: Caused by Parainfluenza virus infections.") 
        print("\nTreatment: Treatment is mainly supportive, including rest, hydration, and sometimes medications to alleviate symptoms such as fever reducers and cough suppressants. In severe cases, hospitalization may be required for respiratory support.")

    elif 'rash' in symptoms or 'sore throat' in symptoms or 'red eyes' in symptoms:
        print("You may have MEASLES VIRUS:")
        print("\nCause: Measles is caused by the measles virus (MeV), a highly contagious virus belonging to the Paramyxoviridae family.") 
        print("\nTreatment: Treatment typically involves supportive care to alleviate symptoms such as fever, cough, and rash.")

    elif ' headache' in symptoms or ' fatigue' in symptoms or 'vomiting' in symptoms:
        print("You may have SWINE FLU:")
        print("\nCause: Swine flu, caused by the H1N1 influenza virus, is transmitted from pigs to humans and occasionally spreads between humans.") 
        print("\nTreatment: Prevention through vaccination, good hygiene practices, and antiviral medications like oseltamivir (Tamiflu) are key in managing swine flu. ")

    elif 'loss of taste' in symptoms or 'fever' in symptoms or 'difficulty breathing'in symptoms :
        print("You may have CORONAVIRUS:")
        print("\nCause: Caused from bats to humans.") 
        print("\nTreatment: Prevention measures such as vaccination, mask-wearing, hand hygiene, and social distancing are crucial.")

if choice == '2':

    symptoms = input("\nPlease enter your symptoms (separated by commas and in lowercase): ")

    if 'body aches' in symptoms or 'weakness' in symptoms or 'fatigue':
        print("You may have INFLUENZA VIRUS:")
        print("\nCause: caused by influenza viruses.") 
        print("\nTreatment: Prevention through annual vaccination, good hygiene practices, and antiviral medications like oseltamivir (Tamiflu) are key in managing influenza.")
        
    elif 'muscle pain'  in symptoms or 'joint pain' in symptoms or 'rash':
        print("You may have DENGUE VIRUS:")
        print("\nCause: Caused by mosquito bites.") 
        print("\nTreatment: Prevention involves avoiding mosquito bites, draining stagnant water, and using insect repellents.")

    elif 'muscle pain'  in symptoms or 'headache' in symptoms or 'rash':
        print("You may have CHIKUNGUNYA VIRUS:")
        print("\nCause: Caused by mainly mosquitos.") 
        print("\nTreatment: there is no specific cure, but supportive treatment can help manage symptoms. Prevention involves avoiding mosquito bites and using insect repellents.")

    elif 'cough'  in symptoms or 'headache' in symptoms or 'shortness of breath':
        print("You may have HANTAVIRUS:")
        print("\nCause: Infection of an eyelash follicle.") 
        print("\nTreatment: Warm compresses and sometimes antibiotics.")

    elif 'weakness' in symptoms or 'muscle aches' in symptoms or 'headache':
        print("You may have West NILE VIRUS:")
        print("\nCause: Infection of an eyelash follicle.") 
        print("\nTreatment: Warm compresses and sometimes antibiotics.")

    elif 'nausea' in symptoms or 'vomiting' in symptoms or 'diarrhea':
        print("You may have  RIFT VALLEY FEVER VIRUS:")
        print("\nCause: Most human infections result from direct or indirect contact with the blood or organs of infected animals.") 
        print("\nTreatment:  there is no specific treatment for RVF, but supportive care can help manage symptoms.")

if choice == '3':

    symptoms = input("\nPlease enter your symptoms (separated by commas and in lowercase): ")

    if 'fever' in symptoms or 'headache' in symptoms or 'swelling of the salivary glands':
        print("You may have MUMPS VIRUS :")
        print("\nCause:  Mumps is highly contagious and spreads through respiratory droplets from coughing, sneezing, or direct contact with an infected person's saliva or mucus.") 
        print("\nTreatment:  there is no specific medicine for mumps, treatment focuses on relieving pain and discomfort.")
        
    elif 'anxiety'  in symptoms or 'headache' in symptoms or 'weakness':
        print("You may have RABIES VIRUS:")
        print("\nCause: It is transmitted through the bite or scratch of an infected animal, most commonly dogs.") 
        print("\nTreatment: Once symptoms develop, there is no cure for rabies, and the disease is almost always fatal.")

    elif 'hearing loss' in symptoms or 'behavioral changes':
        print("You may have MEASLES VIRUS:")
        print("\nCause: primarily spreads through respiratory droplets from coughing and sneezing of an infected person.") 
        print("\nTreatment: There is no specific cure for measles, but supportive care to manage symptoms such as fever, cough, and rash can help.")

    elif 'deafness' in symptoms or 'eye defects':
        print("You may have GERMAN MEASLES: ")
        print("\nCause: known as rubella, is caused by the rubella virus. It spreads through respiratory droplets from coughs and sneezes of an infected person.") 
        print("\nTreatment: Prevention is through vaccination with the measles, mumps, and rubella (MMR) vaccine. There is no specific cure for rubella.")

    elif 'neck stiffness' in symptoms or 'confusion' in symptoms or 'tremors':
        print("You may have ENCEPHALITIS VIRUS :")
        print("\nCause: Caused by bacterial and fungal infections.") 
        print("\nTreatment: Warm compresses and sometimes antibiotics.")

    elif 'confusion' in symptoms or 'muscle weakness' in symptoms or 'paralysis':
        print("You may have WEST NILE VIRUS (WNV):")
        print("\nCause: West Nile virus is primarily transmitted to humans through the bite of infected mosquitoes, particularly those of the Culex species.") 
        print("\nTreatment: Prevention involves measures to avoid mosquito bites, such as using insect repellent, wearing long sleeves and pants, and avoiding outdoor activities during peak mosquito activity times.")

    elif  'paralysis' in symptoms or 'muscle pain' in symptoms or 'fever':
        print("You may have POLIOVIRUS :")
        print("\nCause: primarily spreads through the fecal-oral route, typically contaminating water or food.") 
        print("\nTreatment: There is no cure for poliovirus infection once it occurs, but supportive care can help manage symptoms.")

if choice == '4':

    symptoms = input("\nPlease enter your symptoms (separated by commas and in lowercase): ")

    if 'redness' in symptoms or 'itching' in symptoms or 'pain':
        print("You may have CONJUNCTIVITIS:")
        print("\nCause:bacterial infections can  lead to conjunctivitis.")
        print("\nTreatment:Typically resolves on its own without specific treatment.\nHowever,the following measures may be helpful:")
        print("Use cool compresses to soothe the eyes and reduce discomfort.\n Practice good hygiene, including frequent handwashing and avoiding touching or rubbing the eyes.")
        print("\n Avoid sharing towels, pillowcases, and eye makeup with others to prevent spreading the virus. ")
        
    elif 'pain' in symptoms or 'swelling' in symptoms or 'tears':
        print("You may have STYE:")
        print("\nCause: Infection of an eyelash follicle.") 
        print("\nTreatment: Warm compresses and sometimes antibiotics.")

    elif 'redness' in symptoms or 'blurred vision':
        print("You may have UVEITIS :")
        print("\nCause: Inflammation of the uvea (middle layer of the eye")
        print("\nTreatment: Eye drops, Antiviral Medications,Surgery(In Severe Cases)")

    elif 'redness' in symptoms or 'swelling' in symptoms or 'pain':
        print("You may have CELLULITIS :")
        print("\nCause: Infection of the skin around the eye.")
        print("\nTreatment: Antibiotics, rest, and elevation of the affected area")

    elif 'pain'  in symptoms or 'discharge' in symptoms:
        print("You may have DACRYOCYSTITIS :")
        print("Cause: Infection of the tear sac due to blocked tear ducts.")
        print("Treatment: Warm compresses, antibiotics, and sometimes surgical intervention")
                                              

    elif 'dry eyes' in symptoms or 'redness' in symptoms or 'itching':
        print("You may have BLEPHARITIS :")
        print("\nCauses of Blepharitis:\n")
        print("Allergies: Allergic reactions to environmental allergens, such as pollen, dust, or pet dander, can lead to blepharitis")
        print("Bacterial Infections: Bacteria, particularly Staphylococcus species, can contribute to the development of blepharitis by colonizing the eyelid margins")
        
if choice == '5':

    symptoms = input("\nPlease enter your symptoms (separated by commas and in lowercase): ")

    if 'itching' in symptoms or 'redness' in symptoms:
        print("You may have ECZEMA:")
        print("\nCause: Combination of genetic, immune system, and environmental factors.") 
        print("\nTreatment: Moisturizing the skin regularly, avoiding triggers, using topical corticosteroids or other anti-inflammatory medications, and practicing good skincare habits.")

    elif 'formation of pimples' in symptoms or 'blackheads' in symptoms or 'cysts on the face':
        print("You may have ACNE:")
        print("\nCause: including excess oil production, clogged hair follicles, bacteria (Propionibacterium acnes), hormonal changes, and inflammation..") 
        print("\nTreatment: Oral medications such as antibiotics, hormonal therapies (for women), or isotretinoin may be prescribed for severe cases.")
    
    elif 'persistent redness' in symptoms or 'flushing' in symptoms or 'visible blood vessels':
        print("You may have ROSACEA:")
        print("\nCause: The exact cause of rosacea is unknown, but it may involve genetic, environmental, vascular, and immune system factors.") 
        print("\nTreatment:  Avoiding triggers such as sun exposure, alcohol, spicy foods, and stress. Topical medications (metronidazole, azelaic acid), oral antibiotics, and laser therapy may be prescribed to reduce redness and inflammation.")

    elif 'itching' in symptoms or 'redness' in symptoms or 'inflammation':
        print("You may have CONTACT DERMATITIS:")
        print("\nCause: Contact dermatitis is caused by direct contact with substances that irritate the skin (e.g., detergents, chemicals) or trigger an allergic reaction (e.g., nickel, latex).") 
        print("\nTreatment: Avoiding triggers, applying topical corticosteroids or antihistamines to relieve symptoms, and using emollients or barrier creams to protect the skin.")

    elif 'thickness' in symptoms and 'redness' in symptoms or 'scaly patches':
        print("You may have PSORIASIS:")
        print("\nCause: Psoriasis is an autoimmune disorder where the immune system mistakenly attacks healthy skin cells, leading to rapid turnover of skin cells and inflammation.") 
        print("\nTreatment: Topical corticosteroids, vitamin D analogs, retinoids, and moisturizers. In severe cases, phototherapy (light therapy), oral medications, or biologic drugs may be prescribed.")

if choice == "6" :

    symptoms=input("\n Please enter your symptoms(sesparated by commas in symptoms and in lowercase ):")      

    if "vomitting" in symptoms or "internal and external bleeding" in symptoms or "intense weakness":
        print("You may be suffering from EBOLA VIRUS")
        print("\n Cause: The ebola virus is believed to be animal borne,with bats bieng the most likely reservoir")    
        print("\n Treatment: There is no specific cure for Ebola virus disease (EVD) approved by the FDA. However, supportive care such as maintaining electrolyte balance, providing oxygen therapy, and treating other infections can improve survival")

    elif "nausea and vomiting"in symptoms or "abdominal pain" in symptoms or "facial swelling" in symptoms or "mucosal bleeding":
         print("You may be suffering from LASSA VIRUS")
         print("\n Cause: Lassa virus is caused by infection with the Lassa virus, which is primarily transmitted to humans through contact with food or household items contaminated with rodent urine or feces.")
         print("\n Treatment:: There is no specific cure for Lassa fever, but early supportive care and antiviral treatment can improve outcomes.")

    elif "stiff neck" in symptoms or "coma" in symptoms or "paralysis" in symptoms or "body aches":
        print("You may be suffering from west NILE VIRUS")
        print("\n Cause: It is transmitted through the bites of infected Mosquitoes")
        print("\n Treatment: No cure but depends upon symptoms")

    elif "organ failure" in symptoms or "bleeding from nose,mouth and eyes" in symptoms or "jaundice" in symptoms or "red eyes,face and tounge":
        print("You amy be suffering from yellow fever")
        print("\n Cause: It is caused by the yellow fever virus,which is primarily transmitted to humans through bite of infected mosquitoes")
        print("\n Treatment: By vaccination")

    elif "joint and mucle pain" in symptoms or "difficulty breathing" in symptoms or "cold or clammy skin":
        print("You may be suffering from DENGUE VIRUS")
        print("\n Cause: It is caused by dangue virus")
        print("\n Treatment: There is no treatment but supportive care such as hydration and pain relief ,can help manage manage symptoms")

if choice == "7" :
    
    symptoms=input("\n Please enter your symptoms(sesparated by commas in symptoms and in lowercase ):")  

    if "sneezing" in symptoms or  "blood in the urine" in symptoms or "frequent urination" in symptoms or "rash":
        print("You may be suffering from ADENOVIRUS")
        print("\n Cause: It is spread through close personal contact,respiratory droplets,and conatct eith conataminated surfaces")
        print("\n Treatment: There is no specific antiviral treatment so treatment focuses on managing symptoms ")

    elif "swollen gland" in symptoms or "flu-like symptoms" in symptoms or "pneumonia" in symptoms or "hepatitis":
        print("You may be suffering from CYTOMEGALOVIRUS")
        print("\n Cause: It is caused by close-conatact with body fluids,such as salive,urinr,organ transplantation")
        print("\n Treatment: Antiviral medicines can help manage symptoms and reduce the risk of complication especially in weakened immune system")

    elif "blood in urine" in symptoms or "painful urination" in symptoms or "high blood pressure" in symptoms or "pain in the side or back":
        print("You may be suffering from BK virus")
        print("\n Cause: BK virus is a common virus that usually causes asymptomatic infection but can reactivate in people with weakened immune system")
        print("\n Treatment: There is no specific antiviral treatment but reducing immunosuppression in transplant reciepients and managing symptoms can help ")

    elif "infection" in symptoms or "itching sensation" in symptoms or "burning during urination" in symptoms or "fever":
        print("You may be suffering from Herpes simplex virus ")
        print("\n Cause: It is transmitted through direct contact with infected skin or mucuos membranes")
        print("\n Treatment: There is no cure but antiviral medicines can help and reduce the frequency of outbreaks")

if choice == "8" :
    
    symptoms=input("\n Please enter your symptoms(sesparated by commas in symptoms and in lowercase ):")  

    if "inflammation of heart" in symptoms or "headache" in symptoms or "chest pain" in symptoms or "shortness of breath":
        print("You may be suffering from ENTEROVIRUS")
        print("\n Cause: Spread through close contact with infected person's respiratory secretion,feces,or conatminated surfces ")
        print("\n Treatment: There is no specific antiviral treatment so treatment focuses on managing symptoms ")

    elif "anemia" in symptoms or "joint pain" in symptoms or "arthritis" in symptoms or "immune systewm diorders":
        print("You may be suffering from PARVOVIRUS B19")
        print("\n Cause: It is caused by close-conatact or from person to person")
        print("\n Treatment: Antiviral medicines can help manage symptoms and reduce the risk of complication especially in weakened immune system")

    elif "" in symptoms or "painful urination" in symptoms or "high blood pressure" in symptoms or "pain in the side or back":
        print("You may be suffering from BK VIRUS")
        print("\n Cause: BK virus is a common virus that usually causes asymptomatic infection but can reactivate in people with weakened immune system")
        print("\n Treatment: There is no specific antiviral treatment but reducing immunosuppression in transplant reciepients and managing symptoms can help ")

    elif "infection" in symptoms or "itching sensation" in symptoms or "burning during urination" in symptoms or "fever":
        print("You may be suffering from Herpes simplex virus ")
        print("\n Cause: It is transmitted through direct contact with infected skin or mucuos membranes")
        print("\n Treatment: There is no cure but antiviral medicines can help and reduce the frequency of outbreaks")

        
    

    
