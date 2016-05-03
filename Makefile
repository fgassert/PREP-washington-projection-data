URL = http://cses.washington.edu/picea/mauger/CMIP5/DATA/ps_averages/mat_files/
ALLDATA = all_data_CMIP5_ps_avg.mat
TEMP_CSV = temp_graph.csv
PRECIP_CSV = precip_graph.csv

all: $(TEMP_CSV) $(PRECIP_CSV)

$(TEMP_CSV): $(ALLDATA) process_temp.py
	python process_temp.py $(ALLDATA) $(TEMP_CSV)

$(PRECIP_CSV): $(ALLDATA) process_precip.py
	python process_precip.py $(ALLDATA) $(PRECIP_CSV)

$(ALLDATA):
	curl -O $(URL)$(ALLDATA)

.SECONDARY: *
.PHONY: clean

clean:
	rm -f $(TEMP_CSV) $(PRECIP_CSV)
