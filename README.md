# Project Title

50Core genome Subtyping 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

module load Python/3.7

module load ncbi-blast+/LATEST

module load muscle/3.8.425

module load raxml/8.2.9

module load Entrez/E-utilities

module load prodigal/2.63

pip install -r requirements.txt --user

## Quick Start


``` 
git clone https://git.biotech.cdc.gov/nej1/50scheme.git

cd ~/50scheme/

python pipe1.py ~/50scheme/test1/

```



This script runs entire pipeline from the beginning and get all output results

*base_dir: type 'pwd' in your home directory(i.e./scicomp/home/youruserid/) 

There would be "outputfile" directory at the end of pipeline under
"your_home_directory/your_genome_directory" (i.e./scicomp/home/youruserid/test1/outputfile/)

There would be myscript.log in your home directory that you can check when the pipeline started, each step completed, and finished. 


## Authors

Subin Park

APHL fellow at Centers for Disease control and Prevention

Phone : +1 470 725 5110
Email :nej1@cdc.gov


## License


## Acknowledgments



         
