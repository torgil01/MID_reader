# the program read a mid .csv logfile and convert it to 
# a SPM design file

import sys
import os
import csv
import argparse
import numpy as np
import pandas as pd


def parse_csv(data):
    # header of mid file
    # run.order.file,run.system.seconds_since_epoch,run.system.time,trial.staircase.durationFrames,trial.staircase.thisTrialN,trial.system.seconds_since_epoch,trial.system.time,trial.number,time.onset,trial.response,trial.staircase_stim_duration,trial.rt,trial.stim_duration,trial.should_nudge,trial.reward,total_earnings,fix.after.feedback.adjusted,time.trial,time.run,time.global,subid,session,run,trial.type,fix.after.cue,fix.after.stim,fix.after.feedback,trial.cue_rt,trial.too_fast_rt,participant,session,fMRI? (yes or no),fMRI trigger on TTL? (yes or no),fMRI reverse screen? (yes or no),use ranged rewards?,use nudge for final run?,do only a single behavioral practice run?,start run (0-3),staircase start reward.low,staircase start reward.high,staircase start neutral,staircase start loss.low,staircase start loss.high,date,expName,frameRate,

    # trial.type
    # time.onset
    # trial.response	
    # trial.staircase_stim_duration	
    # trial.rt	
    # trial.stim_duration	
    # trial.should_nudge	
    # trial.reward	
    # total_earnings

    # create a pandas dataframe to store the data
    df = pd.DataFrame(columns=['trial_type', 'onset', 'duration', 'response_time', 'response', 'reward', 'total_earnings'])
    return df

def write_spm(df, out_file):
        # spm design file specs: https://imaging.mrc-cbu.cam.ac.uk/imaging/BasicOnsetFiles
        # the file is a tab-delimited text file with the following columns:
        # trial_type onset duration 
        #  trial_type: the name of the condition has to be a number
        #  onset: the onset of the event in seconds
        #  duration: the duration of the event in seconds
    
    df.to_csv(out_file, sep='\t', index=False)
    

    # open file to write
    f = open(out_file, 'w')
    # write header
    f.write('trial_type\tonset\tduration\n')
    # write data




def main():
    # parse input arguments
    parser = argparse.ArgumentParser(description='Convert mid .csv logfile to SPM design file')
    parser.add_argument('csv', help='input .csv logfile')
    parser.add_argument('out', help='Name of SPM design file')

    args = parser.parse_args()
    # put arguments into variables
    csv_file = args.csv
    out_file = args.out

    # read csv file
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)

    # call function to parse the csv file and return an pandas df with the data
    df = parse_csv(data)

    # call function to write the SPM design file
    write_spm(df, out_file)


if __name__ == "__main__":
    main()