

Scripts for preparing data to recreate these graphs from Abatzoglou and Brown (2011)

![graph](https://raw.githubusercontent.com/fgassert/PREP-washington-projection-data/master/Screen%20Shot%202016-05-03%20at%206.42.22%20PM.png)

### Output files:

- [temp_graph.csv](https://raw.githubusercontent.com/fgassert/PREP-washington-projection-data/master/temp_graph.csv)
- [precip_graph.csv](https://raw.githubusercontent.com/fgassert/PREP-washington-projection-data/master/precip_graph.csv)

### Column names

YEAR: ```year```

Ensemble averages:
- Historical: ```AVG_HIST```
- RCP45: ```AVG_RCP45```
- RCP85: ```AVG_RCP85```

Individual models (background lines)
- Historical: ```hist_*```
- RCP45: ```rcp45_*```
- RCP85: ```rcp85_*```

### Units

- temp_graph.csv: Degrees F from baseline
- precip_graph.csv: Fraction deviation from baseline

### Build

Requires: curl, scipy, numpy, pandas, pylab

```
make clean; make
```
