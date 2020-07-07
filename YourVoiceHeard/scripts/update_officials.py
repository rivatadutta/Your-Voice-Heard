from emailreps.models import Representative, Senator
import csv
import os

def run():
    curr_dir = os.path.dirname(__file__)
    
    reps = Representative.objects.all()
    reps.delete()
    sens = Senator.objects.all()
    sens.delete()
    
    # Update Reps
    with open(os.path.join(curr_dir, './representatives.csv')) as rep_csv:
        csv_reader = csv.reader(rep_csv, delimiter=',')
        line_num = 0
        for row in csv_reader:
            if line_num == 0:
                line_num += 1
                continue
            print()
            print(row[0],row[1],row[2],row[3])
            print()
            rep = Representative(rep_name = row[0], comittee = row[3], website = row[2], state = row[1])
            rep.save()
            line_num += 1

    # Update Sens
    with open(os.path.join(curr_dir, './senators.csv')) as sen_csv:
        csv_reader = csv.reader(sen_csv, delimiter=',')
        line_num = 0
        for row in csv_reader:
            if line_num == 0:
                line_num += 1
                continue
            print()
            print(row[0],row[1],row[2])
            print()
            sen = Senator(sen_name = row[0], website = row[2], state = row[1])
            sen.save()
            line_num += 1
            
    print()
    print(Representative.objects.all())
    print()
    print(Senator.objects.all())
    print()
    
    
    
    