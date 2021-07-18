# 2021-interactive-heat-map

*An explorative approach for interactive heat-maps, using data during swiss heat-wave in 2019, based solely on python.*  

This project was done as a seminar work for "Seminar Geodata Analysis and Modelling" at the University of Bern, 
during the spring semester of 2021.

The data consist of [NetAtmo citizen weather stations (CWS)](https://weathermap.netatmo.com/) measurements.

## Contact Data
Name: Brian Schweigler  
E-Mail: brian.schweigler@students.unibe.ch

## Objectives
- [X] Display CWS  on geospatial map.
- [X] Display relevant (meta-) information on-click of points.
- [ ] Optional: *Animate* data / maps.

## Nice to have:
- [X] Visually appealing display of information.
- [X] Further interactivity (Zoom / Mouse-Over).
- [ ] Interpolation with additional information.

## Project Approach
Primarily, I focused on a minimal working representation of the CWS on a map of Berne.  
From there I went on to include a larger data set.
Next step was finding a way to make the points and map interactable.
Here I migrate from the standard plotting functions to Bokeh, after trying several alternatives.
Bokeh was the easiest to work with and seemed the most flexible in also accomodating GeoData.
Nonetheless, the dataframe had to be adjusted to be imported into Bokeh.

Furthermore, the supervisors had the suggestion of not only making the map interactable, 
but also implementing a way to navigate between time-steps. 
In theory, this sounds feasible, but when dealing with python code, it can not be dynamically recompiled in the browser.
To connect real python callbacks to user events (like clicks), there has to be an actual Python process running to execute the callback code. 
That process could be handled by a Bokeh server (or plain native javascript), but that is outside the scope of this seminar project and would deviate from the native python focus.

## Result
The completed maps can be downloaded as html files and opened in your browser of choosing.  
Alternatively, the following links via github pages can also be used:
- [Bern-CWS-Map_26.06.19 - 22.html](https://unibe-geodata-modelling.github.io/2021-interactive-heat-map/maps/Bern-CWS-Map_26.06.19%20-%2022.html)
- [Bern-CWS-Map_26.06.19 - 23.html](https://unibe-geodata-modelling.github.io/2021-interactive-heat-map/maps/Bern-CWS-Map_26.06.19%20-%2023.html)
- [Bern-CWS-Map_27.06.19 - 00.html](https://unibe-geodata-modelling.github.io/2021-interactive-heat-map/maps/Bern-CWS-Map_27.06.19%20-%2000.html)
- [Bern-CWS-Map_27.06.19 - 01.html](https://unibe-geodata-modelling.github.io/2021-interactive-heat-map/maps/Bern-CWS-Map_27.06.19%20-%2001.html)
- [Bern-CWS-Map_27.06.19 - 02.html](https://unibe-geodata-modelling.github.io/2021-interactive-heat-map/maps/Bern-CWS-Map_27.06.19%20-%2002.html)
- [Bern-CWS-Map_27.06.19 - 03.html](https://unibe-geodata-modelling.github.io/2021-interactive-heat-map/maps/Bern-CWS-Map_27.06.19%20-%2003.html)
- [Bern-CWS-Map_27.06.19 - 04.html](https://unibe-geodata-modelling.github.io/2021-interactive-heat-map/maps/Bern-CWS-Map_27.06.19%20-%2004.html)
- [Bern-CWS-Map_27.06.19 - 05.html](https://unibe-geodata-modelling.github.io/2021-interactive-heat-map/maps/Bern-CWS-Map_27.06.19%20-%2005.html)

**A short rudimentary video demo:**  
![Test](https://github.com/unibe-geodata-modelling/2021-interactive-heat-map/blob/main/videos/demo.gif)


The maps speak for themselves.  

Bokeh is very versatile. 
Ease-of-use is debatable as javascript approaches can be more straight-forward, but if you are working in Python then I can definitely vouch for Bokeh and its functionality.

Alternatives looked at and even partly tested: 
- [plotly](https://plotly.com/python/), 
- [geopandas-view](https://github.com/martinfleis/geopandas-view)
- [hvplot](https://hvplot.holoviz.org/)
- [cartopy](https://scitools.org.uk/cartopy/docs/latest/) - Dependencies are a pain on Windows here!

## Repository Structure
- data: The data used for the scripts. `sample_data.csv` was a substet used for testing from `cws_bern_ta_level_o1_2019_Snippet_UTM.csv`.
- maps: The output html files.
- src: Contains the python files to run, `cws_overview.py` is the jumping off point which uses the other python files. Please execute only that file to reproduce the results.
  -  Each of the files has its own short documentation within them.
- videos: Contains the gif used as a video demonstration.

Github Pages was also set-up to provide the linking of HTML pages, quite an interesting tool.

## Project Requirements
- Python 3.X (Tested on 3.9)
- Bokeh
- Numpy

## Improvements
If one had enough time, there is always a lot to be improved and iterated upon.  
To stay within the frame of the lecture, the following improvements were left out:
- **Higher Resolution of points temperature differences (using more color shades).**  
  Left out as three colors are sufficient for a PoC.
- **Alternatives to OpenStreetMap.**  
  Left out as it would only change the underlying map, but not the interactivity.
- **Fine-tuning of parameters, e.g. point size through a widget.**  
  May be interesting, but leads to visual clutter and is not the intent.
- **Larger time-frame than just a few hours in the nights of 26th to 27th of June 2019.**  
  While this is definitely doable, in the project this was based on, we only focused on that specific night, 
  as the decision-maker Stadtgrün Bern focused on that.  
  [Here's the repository for that project for further information](https://github.com/Brian6330/RIG-HeatMap)

## Acknowledgments
Many thanks to Dr. Andreas Zischg and Dr. Pascal Horton for the seminar and the possibility to do explorative work!
