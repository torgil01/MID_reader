# the program read a mid .csv logfile and convert it to
# a SPM design file


import argparse
import pandas as pd


from datetime import datetime


def parse_csv(data):
    # some of the relavant variables in csv file
    # trial.type
    # time.onset
    # trial.response
    # trial.staircase_stim_duration
    # trial.rt
    # trial.stim_duration
    # time.trial
    # trial.should_nudge
    # trial.reward
    # total_earnings
    

    # remove rows with NA in trial.number column
    data = data.dropna(subset=["trial.number"], ignore_index=True)
    print(data)

    # sort by trial.number
    data = data.sort_values(by=["trial.number"])
    # subtract the first trial onset from all onsets
    data["time.onset"] = data["time.onset"] - data["time.onset"][0]

    # data["time.onset"] = data["time.onset"] - data["time.onset"][0]
    # get subject id from subid column
    id = "id_" + "%03d" % data["subid"][0]
    # get date and time from trial.system.time
    dd = str(data["trial.system.time"][0])
    d =  datetime.strptime(dd, "%a %b %d %H:%M:%S %Y")
    datestr = d.strftime("%Y%m%d")

    # replace spaces in datestr with underscores
    datestr = datestr.replace(" ", "_")
    # create new dataframe from data that only contain the columns trial.type, time.onset, time.trial
    df = data[["trial.type", "time.onset", "time.trial"]]
    # sort df by time.onset
    df = df.sort_values(by=["time.onset"])
    # reset index
    df = df.reset_index(drop=True)
    return df, id, datestr


def write_spm(df, out_file):
    # spm design file specs: https://imaging.mrc-cbu.cam.ac.uk/imaging/BasicOnsetFiles
    # the file is a tab-delimited text file with the following columns:
    # trial_type onset duration
    #  trial_type: the name of the condition has to be a number
    #  onset: the onset of the event in seconds
    #  duration: the duration of the event in seconds

    # must recode trial.type to numbers
    # 1 = reward.low
    # 2 = reward.high
    # 3 = neutral
    # 4 = loss.low
    # 5 = loss.high

    # create new column in df with trial.type recoded to numbers 
    df["trial.type"] = df["trial.type"].replace(
        {
            "reward.low": 1,
            "reward.high": 2,
            "neutral": 3,
            "loss.low": 4,
            "loss.high": 5,
        }
    )

    df.to_csv(out_file, sep="\t", index=False, float_format="%8.1f", header=False)


def main():
    # parse input arguments
    parser = argparse.ArgumentParser(
        description="Convert mid .csv logfile to SPM design file"
    )
    parser.add_argument(
        "-c", help="input .csv logfile", action="store", dest="csv", required=True
    )
    parser.add_argument(
        "-o", help="Name of SPM design file", action="store", dest="out", required=True
    )

    args = parser.parse_args()
    # put arguments into variables
    csv_file = args.csv
    out_file = args.out

    # read csv file into pandas dataframe
    data = pd.read_csv(csv_file)

    # call function to parse the csv file and return a pandas df with relevant data
    df, id, datestr = parse_csv(data)

    # combine id and datestr to create a unique name for the output file
    out_file = str(id) + "_" + datestr + "_" + out_file

    print(df)

    # call function to write the SPM design file
    write_spm(df, out_file)


if __name__ == "__main__":
    main()
