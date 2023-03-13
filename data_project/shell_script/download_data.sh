# echo <variable> prints the command instead of executing it. Useful when creating the script.
# In the video, there's a compression step not needed here cause it's already in .csv.gz format (from GitHub repo).

############## WARNING
#The line below is NECCESSARY for gitbash to execute this script.

#!/bin/bash    

############## WARNING

TAXI_TYPE=$1  #"yellow"       ---> this way we'll pass both values through CLI
YEAR=$2  #2020

set -e              #this makes the code stop at the first non-zero code (in this case it'll be when wget returns '404 Error' for months in 2021 >= than 8, since they're not avalable in the repo).

URL_PREFIX="https://github.com/DataTalksClub/nyc-tlc-data/releases/download"

for MONTH in {1..12}; do
    FMONTH=`printf "%02d" ${MONTH}`     # ---> takes a number and returns it with a special format 
                                          #     (starts with zero and takes last two digits in this case)
    
    URL="${URL_PREFIX}/${TAXI_TYPE}/${TAXI_TYPE}_tripdata_${YEAR}-${FMONTH}.csv.gz"
    
    LOCAL_PREFIX="data/raw/${TAXI_TYPE}/${YEAR}/${FMONTH}"
    LOCAL_FILE="${TAXI_TYPE}_tripdata_${YEAR}_${FMONTH}.csv.gz"
    LOCAL_PATH="${LOCAL_PREFIX}/${LOCAL_FILE}"

    echo "donwloading ${URL} to ${LOCAL_PATH}"
    mkdir -p ${LOCAL_PREFIX}                  # ---> "-p" stand for parent (create all other neccesary directories)
    wget ${URL} -O  ${LOCAL_PATH}     # ---> "-O" is used for specifying where to download it.                          

done


#There's a slight issue with this script: it creates the month folder and the file even though the file doesn't exist in the repo (>= 8 case).