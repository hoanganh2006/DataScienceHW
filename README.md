

```python
import pandas as pd
import numpy as np
import csv
import os
```


```python
#Join path for data and create a data frame for the student data
students = os.path.join('students_complete.csv')
students_df = pd.read_csv(students)
students_df['Passed Reading']= np.where(students_df['reading_score']>=70, 1, 0)
students_df['Passed Math']= np.where(students_df['math_score']>=70, 1, 0)
```


```python
#Import schools data, sort values for the school, create a data frame for data
schools = os.path.join('schools_complete.csv')
schools_df = pd.read_csv(schools)
schools_df = schools_df.sort_values('name').reset_index()
schools_df = schools_df.drop(columns = ['index', 'School ID'])
schools_df = pd.DataFrame(schools_df)
```


```python
school_district = schools_df.loc[schools_df['type'] == 'District', : ]
school_district = pd.DataFrame(school_district)
```


```python
student_district = pd.DataFrame()
for school in school_district['name']:
    student_district = student_district.append(students_df.loc[students_df['school'] == school , :])
```


```python
# Create a high level snapshot (in table form) of the district's key metrics
average_reading_score = student_district['reading_score'].mean()
average_math_score = student_district['math_score'].mean()
total_school = school_district['name'].count()
total_student = school_district['size'].sum()
total_budget = school_district['budget'].sum()
reading_score = student_district.loc[student_district['reading_score'] >= 70, 'reading_score'].count()
passing_reading = (reading_score/total_student)*100
math_score = student_district.loc[student_district['math_score'] >= 70, 'math_score'].count()
passing_math = (math_score/total_student)*100
average_passing = (passing_math + passing_reading)/2
district_summary = pd.DataFrame({"Total Schools": [total_school], "Total Students": [total_student], "Total Budget": [total_budget], "Average Math Score": [average_math_score], "Average Reading Score": [average_reading_score], "% Passing Math": [passing_math], "% Passing Reading" : [passing_reading], "% Overall Passing Rate" : [average_passing]})
district_summary = district_summary[['Total Schools', 'Total Students', 'Total Budget', 'Average Math Score', 'Average Reading Score', '% Passing Math', '% Passing Reading', '% Overall Passing Rate']]
district_summary
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7</td>
      <td>26976</td>
      <td>17347923</td>
      <td>76.987026</td>
      <td>80.962485</td>
      <td>66.518387</td>
      <td>80.905249</td>
      <td>73.711818</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Part 2 for schools summary
summary = pd.DataFrame()
summary[''] = schools_df['name']
summary['School Type'] = schools_df['type']
summary['Total Students'] = schools_df['size']
summary['Total Budget'] = schools_df['budget']
summary['Per Student Budget'] = summary['Total Budget']/summary['Total Students']
summary['Average Reading Score'] = students_df.groupby(students_df['school'])['reading_score'].mean().reset_index().drop(columns = ['school'])
summary['Average Math Score'] = students_df.groupby(students_df['school'])['math_score'].mean().reset_index().drop(columns = ['school'])
reading_passed = students_df.groupby(students_df['school'])['Passed Reading'].sum().reset_index().drop(columns = ['school'])
summary['% Passing Reading'] = (reading_passed['Passed Reading']/schools_df['size'])*100
math_passed = students_df.groupby(students_df['school'])['Passed Math'].sum().reset_index().drop(columns = ['school'])
summary['% Passing Math'] = (math_passed['Passed Math']/schools_df['size'])*100
summary['% Overall Passing Rate'] = (summary['% Passing Reading'] + summary['% Passing Math'])/2
summary.set_index('', inplace = True)
summary
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Per Student Budget</th>
      <th>Average Reading Score</th>
      <th>Average Math Score</th>
      <th>% Passing Reading</th>
      <th>% Passing Math</th>
      <th>% Overall Passing Rate</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
      <td>628.0</td>
      <td>81.033963</td>
      <td>77.048432</td>
      <td>81.933280</td>
      <td>66.680064</td>
      <td>74.306672</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
      <td>582.0</td>
      <td>83.975780</td>
      <td>83.061895</td>
      <td>97.039828</td>
      <td>94.133477</td>
      <td>95.586652</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>639.0</td>
      <td>81.158020</td>
      <td>76.711767</td>
      <td>80.739234</td>
      <td>65.988471</td>
      <td>73.363852</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
      <td>644.0</td>
      <td>80.746258</td>
      <td>77.102592</td>
      <td>79.299014</td>
      <td>68.309602</td>
      <td>73.804308</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>625.0</td>
      <td>83.816757</td>
      <td>83.351499</td>
      <td>97.138965</td>
      <td>93.392371</td>
      <td>95.265668</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>652.0</td>
      <td>80.934412</td>
      <td>77.289752</td>
      <td>80.862999</td>
      <td>66.752967</td>
      <td>73.807983</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>Charter</td>
      <td>427</td>
      <td>248087</td>
      <td>581.0</td>
      <td>83.814988</td>
      <td>83.803279</td>
      <td>96.252927</td>
      <td>92.505855</td>
      <td>94.379391</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>655.0</td>
      <td>81.182722</td>
      <td>76.629414</td>
      <td>81.316421</td>
      <td>65.683922</td>
      <td>73.500171</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
      <td>650.0</td>
      <td>80.966394</td>
      <td>77.072464</td>
      <td>81.222432</td>
      <td>66.057551</td>
      <td>73.639992</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
      <td>609.0</td>
      <td>84.044699</td>
      <td>83.839917</td>
      <td>95.945946</td>
      <td>94.594595</td>
      <td>95.270270</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>637.0</td>
      <td>80.744686</td>
      <td>76.842711</td>
      <td>80.220055</td>
      <td>66.366592</td>
      <td>73.293323</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>600.0</td>
      <td>83.725724</td>
      <td>83.359455</td>
      <td>95.854628</td>
      <td>93.867121</td>
      <td>94.860875</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
      <td>638.0</td>
      <td>83.848930</td>
      <td>83.418349</td>
      <td>97.308869</td>
      <td>93.272171</td>
      <td>95.290520</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
      <td>578.0</td>
      <td>83.989488</td>
      <td>83.274201</td>
      <td>96.539641</td>
      <td>93.867718</td>
      <td>95.203679</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>Charter</td>
      <td>1800</td>
      <td>1049400</td>
      <td>583.0</td>
      <td>83.955000</td>
      <td>83.682222</td>
      <td>96.611111</td>
      <td>93.333333</td>
      <td>94.972222</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Top 5 schools have the highest overall passing rate
top_5 = summary.sort_values('% Overall Passing Rate').tail()
top_5
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Per Student Budget</th>
      <th>Average Reading Score</th>
      <th>Average Math Score</th>
      <th>% Passing Reading</th>
      <th>% Passing Math</th>
      <th>% Overall Passing Rate</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Wilson High School</th>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
      <td>578.0</td>
      <td>83.989488</td>
      <td>83.274201</td>
      <td>96.539641</td>
      <td>93.867718</td>
      <td>95.203679</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>625.0</td>
      <td>83.816757</td>
      <td>83.351499</td>
      <td>97.138965</td>
      <td>93.392371</td>
      <td>95.265668</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
      <td>609.0</td>
      <td>84.044699</td>
      <td>83.839917</td>
      <td>95.945946</td>
      <td>94.594595</td>
      <td>95.270270</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
      <td>638.0</td>
      <td>83.848930</td>
      <td>83.418349</td>
      <td>97.308869</td>
      <td>93.272171</td>
      <td>95.290520</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
      <td>582.0</td>
      <td>83.975780</td>
      <td>83.061895</td>
      <td>97.039828</td>
      <td>94.133477</td>
      <td>95.586652</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Bottom 5 schools have the lowest overall passing rate
bottom_5 = summary.sort_values('% Overall Passing Rate').head()
bottom_5
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Per Student Budget</th>
      <th>Average Reading Score</th>
      <th>Average Math Score</th>
      <th>% Passing Reading</th>
      <th>% Passing Math</th>
      <th>% Overall Passing Rate</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Rodriguez High School</th>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>637.0</td>
      <td>80.744686</td>
      <td>76.842711</td>
      <td>80.220055</td>
      <td>66.366592</td>
      <td>73.293323</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>639.0</td>
      <td>81.158020</td>
      <td>76.711767</td>
      <td>80.739234</td>
      <td>65.988471</td>
      <td>73.363852</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>655.0</td>
      <td>81.182722</td>
      <td>76.629414</td>
      <td>81.316421</td>
      <td>65.683922</td>
      <td>73.500171</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
      <td>650.0</td>
      <td>80.966394</td>
      <td>77.072464</td>
      <td>81.222432</td>
      <td>66.057551</td>
      <td>73.639992</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
      <td>644.0</td>
      <td>80.746258</td>
      <td>77.102592</td>
      <td>79.299014</td>
      <td>68.309602</td>
      <td>73.804308</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Create a dataframe of math score by grade for each school 
math_score_by_grade = students_df.groupby(['school', 'grade'])['math_score'].mean().reset_index()
math_score_by_grade = math_score_by_grade.rename(columns = {'school': '', 'grade': ' ', 'math_score': 'Math Score'})
math_score_by_grade = math_score_by_grade.pivot(index = '', columns=' ', values='Math Score')
math_score_by_grade
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
      <th>9th</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>76.996772</td>
      <td>77.515588</td>
      <td>76.492218</td>
      <td>77.083676</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.154506</td>
      <td>82.765560</td>
      <td>83.277487</td>
      <td>83.094697</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>76.539974</td>
      <td>76.884344</td>
      <td>77.151369</td>
      <td>76.403037</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>77.672316</td>
      <td>76.918058</td>
      <td>76.179963</td>
      <td>77.361345</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>84.229064</td>
      <td>83.842105</td>
      <td>83.356164</td>
      <td>82.044010</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.337408</td>
      <td>77.136029</td>
      <td>77.186567</td>
      <td>77.438495</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.429825</td>
      <td>85.000000</td>
      <td>82.855422</td>
      <td>83.787402</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>75.908735</td>
      <td>76.446602</td>
      <td>77.225641</td>
      <td>77.027251</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>76.691117</td>
      <td>77.491653</td>
      <td>76.863248</td>
      <td>77.187857</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.372000</td>
      <td>84.328125</td>
      <td>84.121547</td>
      <td>83.625455</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>76.612500</td>
      <td>76.395626</td>
      <td>77.690748</td>
      <td>76.859966</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>82.917411</td>
      <td>83.383495</td>
      <td>83.778976</td>
      <td>83.420755</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.087886</td>
      <td>83.498795</td>
      <td>83.497041</td>
      <td>83.590022</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.724422</td>
      <td>83.195326</td>
      <td>83.035794</td>
      <td>83.085578</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>84.010288</td>
      <td>83.836782</td>
      <td>83.644986</td>
      <td>83.264706</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Create a dataframe of reading score by grade for each school 
reading_score_by_grade = students_df.groupby(['school', 'grade'])['reading_score'].mean().reset_index()
reading_score_by_grade = reading_score_by_grade.rename(columns = {'school': '', 'grade': ' ', 'reading_score': 'Reading Score'})
reading_score_by_grade = reading_score_by_grade.pivot(index = '', columns=' ', values='Reading Score')
reading_score_by_grade
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
      <th>9th</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>80.907183</td>
      <td>80.945643</td>
      <td>80.912451</td>
      <td>81.303155</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>84.253219</td>
      <td>83.788382</td>
      <td>84.287958</td>
      <td>83.676136</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>81.408912</td>
      <td>80.640339</td>
      <td>81.384863</td>
      <td>81.198598</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>81.262712</td>
      <td>80.403642</td>
      <td>80.662338</td>
      <td>80.632653</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>83.706897</td>
      <td>84.288089</td>
      <td>84.013699</td>
      <td>83.369193</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>80.660147</td>
      <td>81.396140</td>
      <td>80.857143</td>
      <td>80.866860</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.324561</td>
      <td>83.815534</td>
      <td>84.698795</td>
      <td>83.677165</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>81.512386</td>
      <td>81.417476</td>
      <td>80.305983</td>
      <td>81.290284</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>80.773431</td>
      <td>80.616027</td>
      <td>81.227564</td>
      <td>81.260714</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.612000</td>
      <td>84.335938</td>
      <td>84.591160</td>
      <td>83.807273</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>80.629808</td>
      <td>80.864811</td>
      <td>80.376426</td>
      <td>80.993127</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.441964</td>
      <td>84.373786</td>
      <td>82.781671</td>
      <td>84.122642</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>84.254157</td>
      <td>83.585542</td>
      <td>83.831361</td>
      <td>83.728850</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>84.021452</td>
      <td>83.764608</td>
      <td>84.317673</td>
      <td>83.939778</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.812757</td>
      <td>84.156322</td>
      <td>84.073171</td>
      <td>83.833333</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Scores by School Spending
school_spending = summary.drop(columns = ['School Type', 'Total Budget'])
school_spending['Reading'] = (school_spending['Average Reading Score'] * school_spending['Total Students']).astype(int)
school_spending['Math'] = (school_spending['Average Math Score'] * school_spending['Total Students']).astype(int)
school_spending['Number Passed Reading'] = (school_spending['% Passing Reading'] * school_spending['Total Students']/100).astype(int)
school_spending['Number Passed Math'] = (school_spending['% Passing Math'] * school_spending['Total Students']/100).astype(int)
school_spending = school_spending.drop(columns = ['Average Reading Score', 'Average Math Score', '% Passing Reading', '% Passing Math', '% Overall Passing Rate'])
```


```python
#Create a new dataframe for the school spending result
average_reading = []
average_math = []
percent_reading = []
percent_math = []
less_585 = school_spending.loc[school_spending['Per Student Budget'] < float(585), : ]
average_reading.append(less_585['Reading'].sum()/less_585['Total Students'].sum())
average_math.append(less_585['Math'].sum()/less_585['Total Students'].sum())
percent_reading.append((less_585['Number Passed Reading'].sum()/less_585['Total Students'].sum())*100)
percent_math.append((less_585['Number Passed Math'].sum()/less_585['Total Students'].sum())*100)

more_585 = school_spending.loc[(float(585) <= school_spending['Per Student Budget']) & (float(615) > school_spending['Per Student Budget']), : ]
average_reading.append(more_585['Reading'].sum()/more_585['Total Students'].sum())
average_math.append(more_585['Math'].sum()/more_585['Total Students'].sum())
percent_reading.append((more_585['Number Passed Reading'].sum()/more_585['Total Students'].sum())*100)
percent_math.append((more_585['Number Passed Math'].sum()/more_585['Total Students'].sum())*100)

more_615 = school_spending.loc[(float(615) <= school_spending['Per Student Budget']) & (float(645) > school_spending['Per Student Budget']), : ]
average_reading.append(more_615['Reading'].sum()/more_615['Total Students'].sum())
average_math.append(more_615['Math'].sum()/more_615['Total Students'].sum())
percent_reading.append((more_615['Number Passed Reading'].sum()/more_615['Total Students'].sum())*100)
percent_math.append((more_615['Number Passed Math'].sum()/more_615['Total Students'].sum())*100)

more_645 = school_spending.loc[(float(645) <= school_spending['Per Student Budget']) & (float(675) > school_spending['Per Student Budget']), : ]
average_reading.append(more_645['Reading'].sum()/more_645['Total Students'].sum())
average_math.append(more_645['Math'].sum()/more_645['Total Students'].sum())
percent_reading.append((more_645['Number Passed Reading'].sum()/more_645['Total Students'].sum())*100)
percent_math.append((more_645['Number Passed Math'].sum()/more_645['Total Students'].sum())*100)


result = pd.DataFrame({"Spending Ranges (Per Student)": ["<$585", "$585-615", "$615-645", "$645-675"],"Average Math Score": average_math, "Average Reading Score" : average_reading, "% Passing Math": percent_math, "% Passing Reading": percent_reading})
result['% Overall Passing Rate'] = (result['% Passing Math'] + result['% Passing Reading'])/2
result = result[['Spending Ranges (Per Student)', 'Average Math Score', 'Average Reading Score', '% Passing Math', '% Passing Reading', '% Overall Passing Rate']]
result.set_index('Spending Ranges (Per Student)', inplace = True)
result
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
    <tr>
      <th>Spending Ranges (Per Student)</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;$585</th>
      <td>83.363065</td>
      <td>83.964039</td>
      <td>93.702889</td>
      <td>96.686558</td>
      <td>95.194724</td>
    </tr>
    <tr>
      <th>$585-615</th>
      <td>83.529196</td>
      <td>83.838414</td>
      <td>94.087404</td>
      <td>95.850165</td>
      <td>94.968784</td>
    </tr>
    <tr>
      <th>$615-645</th>
      <td>78.061578</td>
      <td>81.434031</td>
      <td>71.400428</td>
      <td>83.614770</td>
      <td>77.507599</td>
    </tr>
    <tr>
      <th>$645-675</th>
      <td>77.049297</td>
      <td>81.005604</td>
      <td>66.230813</td>
      <td>81.109397</td>
      <td>73.670105</td>
    </tr>
  </tbody>
</table>
</div>




```python
reading = []
math = []
percentage_math = []
percentage_reading = []
small = school_spending.loc[school_spending['Total Students'] < 1000, : ]
reading.append(small['Reading'].sum()/small['Total Students'].sum())
math.append(small['Math'].sum()/small['Total Students'].sum())
percentage_reading.append((small['Number Passed Reading'].sum()/small['Total Students'].sum())*100)
percentage_math.append((small['Number Passed Math'].sum()/small['Total Students'].sum())*100)

medium = school_spending.loc[(1000 <= school_spending['Total Students']) & (2000 > school_spending['Total Students']), : ]
reading.append(medium['Reading'].sum()/medium['Total Students'].sum())
math.append(medium['Math'].sum()/medium['Total Students'].sum())
percentage_reading.append((medium['Number Passed Reading'].sum()/medium['Total Students'].sum())*100)
percentage_math.append((medium['Number Passed Math'].sum()/medium['Total Students'].sum())*100)

large = school_spending.loc[(2000 <= school_spending['Total Students']) & (5000 > school_spending['Total Students']), : ]
reading.append(large['Reading'].sum()/large['Total Students'].sum())
math.append(large['Math'].sum()/large['Total Students'].sum())
percentage_reading.append((large['Number Passed Reading'].sum()/large['Total Students'].sum())*100)
percentage_math.append((large['Number Passed Math'].sum()/large['Total Students'].sum())*100)

result_2 = pd.DataFrame({"School Size": ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"],"Average Math Score":math, "Average Reading Score" :reading, "% Passing Math": percentage_math, "% Passing Reading": percentage_reading})
result_2['% Overall Passing Rate'] = (result_2['% Passing Math'] + result_2['% Passing Reading'])/2
result_2 = result_2[['School Size', 'Average Math Score', 'Average Reading Score', '% Passing Math', '% Passing Reading', '% Overall Passing Rate']]
result_2.set_index('School Size', inplace = True)
result_2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School Size</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Small (&lt;1000)</th>
      <td>83.828654</td>
      <td>83.974082</td>
      <td>93.952484</td>
      <td>95.968323</td>
      <td>94.960403</td>
    </tr>
    <tr>
      <th>Medium (1000-2000)</th>
      <td>83.372682</td>
      <td>83.867989</td>
      <td>93.604788</td>
      <td>96.773058</td>
      <td>95.188923</td>
    </tr>
    <tr>
      <th>Large (2000-5000)</th>
      <td>77.477562</td>
      <td>81.198640</td>
      <td>68.652380</td>
      <td>82.125158</td>
      <td>75.388769</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Create a for loop function for charter school type
school_charter = schools_df.loc[schools_df['type'] == 'Charter', : ]
student_charter = pd.DataFrame()
for school in school_charter['name']:
    student_charter = student_charter.append(students_df.loc[students_df['school'] == school , :])
```


```python
# Create a high level snapshot (in table form) of the charter's key metrics
average_reading_score_1 = student_charter['reading_score'].mean()
average_math_score_1 = student_charter['math_score'].mean()
total_student_1 = school_charter['size'].sum()
reading_passed_1 = ((student_charter['Passed Reading'].sum())/total_student_1)*100
math_passed_1 = ((student_charter['Passed Math'].sum())/total_student_1)*100
average_passing_1 = (math_passed_1 + reading_passed_1)/2
charter_summary = pd.DataFrame({"School Type": "Charter", "Average Math Score": [average_math_score_1], "Average Reading Score": [average_reading_score_1], "% Passing Math": [math_passed_1], "% Passing Reading" : [reading_passed_1], "% Overall Passing Rate" : [average_passing_1]})
charter_summary = charter_summary[['School Type','Average Math Score', 'Average Reading Score', '% Passing Math', '% Passing Reading', '% Overall Passing Rate']]
```


```python
district_summary_1 = district_summary.drop(columns = ['Total Schools', 'Total Students', 'Total Budget'])
district_summary_1['School Type'] = "District"
district_summary_1 = district_summary_1[['School Type','Average Math Score', 'Average Reading Score','% Passing Math','% Passing Reading', '% Overall Passing Rate']]
```


```python
by_school_type = pd.concat([charter_summary, district_summary_1])
by_school_type.set_index('School Type', inplace = True)
by_school_type
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School Type</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Charter</th>
      <td>83.406183</td>
      <td>83.902821</td>
      <td>93.701821</td>
      <td>96.645891</td>
      <td>95.173856</td>
    </tr>
    <tr>
      <th>District</th>
      <td>76.987026</td>
      <td>80.962485</td>
      <td>66.518387</td>
      <td>80.905249</td>
      <td>73.711818</td>
    </tr>
  </tbody>
</table>
</div>


