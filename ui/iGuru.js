function loadQuestions(c_list) {
	var k=0;
	for (i in c_list) { 
		cluster=c_list[i];
		var p= document.createElement("p");
		p.setAttribute('align','left');
		var no = parseInt(i)+1;
		p.innerHTML = p.innerHTML + "Question Set "+no+"<BR>"+".....................................";
		document.getElementById("data").appendChild(p);
		for (j in cluster) {
			//q_list[k]=cluster[j];	
			//k=k+1;
			var parts=cluster[j].split(":::");
			var len=parts[0].length;
			var qid=parts[0].substr(2,len-6);
			var qtext=parts[1];
			var a = document.createElement('a');
			var linkText = document.createTextNode("More");
			a.appendChild(linkText);
			a.title = qid;
			a.href = "http://www.careercup.com/question?id="+qid;
			var p= document.createElement("p");
			p.innerHTML = p.innerHTML + qtext + " ";
			p.setAttribute('align','left');
			p.appendChild(a);
			document.getElementById("data").appendChild(p);
			//document.body.appendChild(a);
		}
	}
	document.getElementById("data").focus();
	//});

}


function showChart1() {

var diameter = 500,
    format = d3.format(",d");

var pack = d3.layout.pack()
    .size([diameter, diameter])
    .value(function(d) { return d.size; });

var svg = d3.select("chart").append("svg")
    .attr("width", diameter)
    .attr("height", diameter)
  .append("g")
    .attr("transform", "translate(0,0)");

var company = document.getElementById('company1').value;


d3.json("ui_11.txt", function(error, root) {
  	if (error) return alert(error);
  	list=root["children"];
	
  	var packdata;
  	for (var item in list) {
		dict=list[item];
		if (dict["name"]==company) {
			packdata=dict;	
		}
  	}

  	var node = svg.datum(packdata).selectAll(".node")
      	.data(pack.nodes)
    	.enter().append("g")
      	.attr("class", function(d) { return d.children ? "node" : "leaf node"; })
      	.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

  	node.append("title")
      	.text(function(d) { return d.name + (d.children ? "" : ": " + format(d.size)); });

  	node.append("circle")
      	.attr("r", function(d) { return d.r; });

  	node.filter(function(d) { return !d.children; }).append("text")
      	.attr("dy", ".3em")
      	.style("text-anchor", "middle")
      	.text(function(d) { return d.name.substring(0, d.r / 3); });
});
}

function showChart2() {

var diameter = 900,
    format = d3.format(",d");

var company1 = document.getElementById('company1').value;
var company2 = document.getElementById('company2').value;

d3.json("ui_2.json", function(error, root) {
  	if (error) return alert(error);
	var found=0;
	var comb;
	for (i in root) {
		comb=root[i];
		if (company1==comb["c1"]) {
			if(company2==comb["c2"]) {
				found=1;
			}
			
		}
		else if (company1==comb["c2"]) {
		 	if(company2==comb["c1"]) {
				found=1;
			}
		}
	}

	if (found==0) {
		return;
	}

	
	var svg = d3.select("chart").append("svg")
		  .attr("width", diameter)
		  .attr("height", diameter/1.5)
		  .append("g")
	    	  .attr("transform", "translate(0,25)");
	
//	alert("inside cluster3c load");
	var node = svg.selectAll(".node") //its implicitly understood that the one that follows t tag also brings to t
	      	.data([{"r":100,"x":100,"y":100,"c":"Microsoft","t":"Algos"},{"r":50,"x":180,"y":100,"c":"Amazon","t":""},
		{"r":100,"x":400,"y":100,"c":"Microsoft","t":"Hash Tables"},{"r":50,"x":480,"y":100,"c":"Amazon","t":""},
		{"r":100,"x":100,"y":400,"c":"Microsoft","t":"Strings"},{"r":50,"x":180,"y":400,"c":"Amazon","t":""}])
	    	.enter().append("g")
	      	.attr("class", function(d) { return "node"; })
	      	.attr("transform", function(d) { return "translate(" + d["x"] + "," + d["y"] + ")"; });

  	node.append("title")
      	.text(function(d) { return d["c"]; });

  	node.append("circle")
      	.attr("r", function(d) { return d["r"]; });

  	node.append("text")
      	.attr("dy", ".3em")
      	.style("text-anchor", "middle")
      	.text(function(d) { return d["c"]; });

	node.append("text")
	//.attr("x",function(d) {return d["x"]-d["r"]-10;})
	//.attr("y",function(d) {return d["y"]-d["r"]-10;})
      	.attr("dy", function(d) {return (-1)*(parseInt(d["r"])+5);})
	.text(function(d) {return d["t"];});




});

}

function showDistribution() {

d3.select("svg")
       .remove();

d3.select("#tform").remove();
d3.select("body").append("div").attr("id","tform").attr("align","center");

d3.select("#data").remove();
d3.select("body").append("div").attr("id","data").attr("align","center");

var company2e = document.getElementById("company2");

if (company2e==null) {
	//showChart1();
}
else {
	showChart2();
}

var f = document.createElement("form");
var i = document.createElement("input");
f.innerHTML = f.innerHTML + 'Type a focus area and then click submit to browse the questions <BR>';
i.setAttribute('type',"text");
i.setAttribute('name',"inputbox2");
i.setAttribute('id',"qtag");
i.setAttribute('placeholder',"E.g: Arrays");
var b = document.createElement("input");
b.setAttribute('type',"button");
b.setAttribute('name',"button2");
b.setAttribute('value',"Submit");
b.setAttribute('onClick',"showQuestions()");
f.appendChild(i);
f.appendChild(b);
var p= document.createElement("p");
p.appendChild(f);
document.getElementById("tform").appendChild(p);

}

function showQuestions() {

//alert("entered show questions");

d3.select("#data").remove();
d3.select("body").append("div").attr("id","data").attr("align","center");


var company2e = document.getElementById("company2");

if (company2e==null) {
	//alert("inside correct json load");
	d3.json("Cluster_1_company.txt", function(error, root) {
  	if (error) return alert(error);
	var company = document.getElementById('company1').value;
	var qtag = document.getElementById('qtag').value;
  	c_dict=root[company];
	var c_list=c_dict[qtag];
	if (c_list!=null) {
		alert("c_list loaded properly");
	}
	loadQuestions(c_list);
	});
}
else {
	d3.json("Cluster_2_company.txt", function(error, list) {
  	if (error) return alert(error);
	var company1 = document.getElementById('company1').value;
	var company2 = document.getElementById('company2').value;
	var qtag = document.getElementById('qtag').value;
  	//c_dict=root[company];
	var c_dict=null;
	for (i in list) {
		dict=list[i];
		if ((dict["c2"]==company2) && (dict["c1"]==company1)) {
			c_dict=dict["data"];
			break;
		}
		else if((dict["c1"]==company2) && (dict["c2"]==company1)) {
			c_dict=dict["data"];
			break
		}
	}
	if (c_dict==null) {
		return;
	}
	c_list=c_dict[qtag];
	loadQuestions(c_list);
	});
}
}



