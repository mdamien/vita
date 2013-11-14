$('.service-details a').click(function (e) {
  e.preventDefault()
  $(this).tab('show')
})

$('.service-visible').click(function (e) {
	$(this).parent().find('.service-details').slideToggle(0);
})

var container = document.getElementById("graph1"),
d1 = [[0, 3], [4, 8], [8, 5], [9, 13]],
d2 = [],
options = {
  xaxis: {
    minorTickFreq: 4
  }, 
  grid: {
    minorVerticalLines: true
  }
},
i, graph;

// Generated second data set:
for (i = 0; i < 14; i += 0.5) {
d2.push([i, Math.sin(i)]);
}

graph = Flotr.draw(
	container,
	[ d1, d2 ],
	options 
);