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
    // .padding(.5);

var yLinearScale = d3
    .scaleLinear()
    .range([chartHeight,0]);

    
// Load Data
d3.csv('data.csv',function(error,data){
    if (error) throw error;
    // console.log(data)
    data.forEach(function(element) {
        element.Poverty = +element.Poverty;
        element.HighSchool = +element.HighSchool;})
        console.log(data)

    xBandScale
    .domain(d3.extent(data,d => d.Poverty))
    .nice();
   
    yLinearScale 
    .domain(d3.extent(data,d => d.HighSchool))
    .nice();

    var thing = d3.max(data,function(response){
        return response.Poverty});

    console.log(thing);

    var xaxis = d3.axisBottom(xBandScale);
    var yaxis = d3.axisLeft(yLinearScale);

    svg
    .selectAll("circle")
    .data(data)
    .enter()
        .append('circle')
        .attr('cx', d => xBandScale(d.Poverty))
        .attr('cy', d => yLinearScale(d.HighSchool))
        .attr('r',10)
        .style("stroke", "steelblue")
        .attr("fill-opacity", .6)
        .attr("fill", "steelblue");
    svg
    .selectAll("text")
    .data(data)
    .enter()
        .append('text')
        .attr('x', d => xBandScale(d.Poverty))
        .attr('y', d => yLinearScale(d.HighSchool-.1))
        .style('text-anchor','middle')
        .text(d=>d.State)
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
    .text("Percentage w/out Secondary Education")
    .attr("font-size",15)
    .attr("font-family","sans-serif");      
  
})
