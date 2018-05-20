var svgWidth = window.innerWidth;
var svgHeight = window.innerHeight;

var margin = {
    top: 30,
    right: 30,
    bottom: 50,
    left: 100
};

var chartWidth = svgWidth - margin.left - margin.right;
var chartHeight = svgHeight - margin.top - margin.bottom;

var svg = d3
    .select('body')
    .attr('class','svg-area')
    .append('svg')
    .attr('height',svgHeight)
    .attr('width',svgWidth)
    .append('g')
    .attr("height", chartHeight)
    .attr("width", chartWidth)
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var xBandScale = d3
    .scaleLinear()
    .range([0,chartWidth])

var yLinearScale = d3
    .scaleLinear()
    .range([chartHeight,0]);

    
// Load Data
d3.csv("./data.csv", function(error, data) {
    if (error) console.error;
    console.log(data);
    // log a list of names
    var names = data.map(data => data.poverty);
    console.log("poverty", names);

  // Cast the hours value to a number for each piece of tvData
//   tvData.forEach(function (data) {
//     data.hours = +data.hours;
//     console.log("Name:", data.name);
//     console.log("Hours:", data.hours);
// });

    xBandScale
    .domain(d3.extent(data,d => d.poverty))
    .nice();
   
    yLinearScale 
    .domain(d3.extent(data,d => d.healthcare))
    .nice();

    var dataPoint = d3.max(data,function(response){
        return response.poverty});

    console.log(dataPoint);

    var xaxis = d3.axisBottom(xBandScale);
    var yaxis = d3.axisLeft(yLinearScale);

    svg
    .selectAll("circle")
    .data(data)
    .enter()
        .append('circle')
        .attr('cx', d => xBandScale(d.poverty))
        .attr('cy', d => yLinearScale(d.healthcare))
        .attr('r',10)
        .style("stroke", "steelblue")
        .attr("fill-opacity", .6)
        .attr("fill", "steelblue");
    svg
    .selectAll("text")
    .data(data)
    .enter()
        .append('text')
        .attr('x', d => xBandScale(d.poverty))
        .attr('y', d => yLinearScale(d.healthcare-.1))
        .style('text-anchor','middle')
        .text(d=>d.abb)
        .attr("fill", "white")
        .attr("font-size",10)
        .attr("font-family","sans-serif");
    
    svg
    .append("g")
    .attr("transform", "translate(0," + chartHeight + ")")
    .call(xaxis);

    svg
    .append("text")             
    .attr("transform",
          "translate(" + (chartWidth/2) + " ," + 
                         (chartHeight + (margin.top * 1.5) ) + ")")
    .style("text-anchor", "middle")
    .text("Percentage in Poverty")
    .attr("font-size",15)
    .attr("font-family","sans-serif");
    
    svg
    .append("g")
    .call(yaxis);
    svg
    .append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 0 - (.5*margin.left))
    .attr("x",0 - (chartHeight / 2))
    .attr("dy", "1em")
    .style("text-anchor", "middle")
    .text("Percentage without Healthcare")
    .attr("font-size",15)
    .attr("font-family","sans-serif");      
});



