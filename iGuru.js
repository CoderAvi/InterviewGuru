var distr1="ui_11.txt";
var distr2="ui_2.json"; //not important
var questions1="Cluster_1_total.txt";
var questions2="total_cluster.txt";



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

//alert("Entered ShowChart");

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

var company1se = document.getElementById('company1s');

var company = company1se.options[company1se.selectedIndex].text;
//alert("printing"+company);


d3.json(distr1, function(error, root) {
  	if (error) return alert("can't read distr1 file");
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

var company1se = document.getElementById('company1s').value;
var company1 = company1se.options[company1se.selectedIndex].text;

var company2se = document.getElementById('company2s').value;
var company2 = company2se.options[company2se.selectedIndex].text;

d3.json(distr2, function(error, root) {
  	if (error) return alert("can't read distr2 file");
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
function listContains(list,value) {
	for (i in list) {
		if (value==list[i]) {
			return true;
		}
	}
	return false;
}

function popCompanyList() {
    var company2se = document.getElementById("company2s");
    if (company2se==null) {
	d3.json(distr1, function(error, root) {
		if (error) return alert("can't read distr1 file");
  		list=root["children"];
		var companies=[];
 	 	for (var item in list) {
			dict=list[item];
			companies[item]=dict["name"];
  		}
		popSelectBox("company1s",companies);
	});
    }
    else {
	d3.json(questions2, function(error, list) {
	  	if (error) return alert("can't read questions2 file");
		var companies1=[];
		var companies2=[];
		var j=0,k=0;
 	 	for (var item in list) {
			dict=list[item];
			if (!listContains(companies1,dict["c1"])) {
				companies1[j]=dict["c1"];
				j=j+1;
			}
			if (!listContains(companies2,dict["c2"])) {
				companies2[k]=dict["c2"];
				k=k+1;
			}
  		}
		popSelectBox("company1s",companies1);
		popSelectBox("company2s",companies2);
	});
    }
}


function popSelectBox(selboxID,optionList) {
   for(i in optionList) {
	option=optionList[i];
	var o= document.createElement("option");
	o.setAttribute("value",option);
	o.innerHTML = o.innerHTML + option;
	var selbox=document.getElementById(selboxID);
	selbox.appendChild(o);
   }
}


function showDistribution() {

//alert("Entered Distr");

d3.select("svg")
       .remove();

d3.select("#tform").remove();
d3.select("body").append("div").attr("id","tform").attr("align","center");

d3.select("#data").remove();
d3.select("body").append("div").attr("id","data").attr("align","center");

var company2se = document.getElementById("company2s");

if (company2se==null) {
	showChart1();
}
else {
	//showChart2();
}


var f = document.createElement("form");

f.innerHTML = f.innerHTML + 'Type a focus area and then click submit to browse the questions <BR>';


/*
var i = document.createElement("input");
i.setAttribute('type',"text");
i.setAttribute('name',"inputbox2");
i.setAttribute('id',"qtag");
i.setAttribute('placeholder',"E.g: Arrays");
*/
var s = document.createElement("select");
s.setAttribute('id','qtags');






var b = document.createElement("input");
b.setAttribute('type',"button");
b.setAttribute('name',"button2");
b.setAttribute('value',"Submit");
b.setAttribute('onClick',"showQuestions()");
f.appendChild(s);
f.appendChild(b);
var p= document.createElement("p");
p.appendChild(f);
document.getElementById("tform").appendChild(p);

var company2se = document.getElementById('company2s');
var company2 = null;
if (company2se!=null) {
	d3.json(questions2, function(error, list) {
  	if (error) return alert("can't read questions2 file");
	var company1se = document.getElementById('company1s');
	var company2se = document.getElementById('company2s');
	var company1 = company1se.options[company1se.selectedIndex].text;
	var company2 = company2se.options[company2se.selectedIndex].text;
	var tlist=[];
	var c_dict=null;
	for (i in list) {
		dict=list[i];
		if ((dict["c2"]==company2) && (dict["c1"]==company1)) {
			c_dict=dict["data"];
			break;
		}
	}
	tlist=Object.keys(c_dict);
	popSelectBox("qtags",tlist);
	});
}
else {	
	//alert("custom entered");
	//alert("questions1"+questions1);
	d3.json(questions1, function(error, root) {
  	if (error) return alert("can't read questions1 file");
	var e = document.getElementById('company1s')
	var company=e.options[e.selectedIndex].text;
	//alert("did i "+company);
  	c_dict=root[company];
	var tlist=Object.keys(c_dict);
	//alert("list"+tlist);
	popSelectBox("qtags",tlist);
	});
}
	

//alert("no error till this point");


}

function showQuestions() {

//alert("entered show questions");

d3.select("#data").remove();
d3.select("body").append("div").attr("id","data").attr("align","center");


var company2se = document.getElementById("company2s");

if (company2se==null) {
	//alert("inside correct json load");
	d3.json(questions1, function(error, root) {
  	if (error) return alert("can't read questions1 file");
	var e = document.getElementById('company1s');
	var company=e.options[e.selectedIndex].text;
	var qtage = document.getElementById('qtags');
	var qtag=qtage.options[qtage.selectedIndex].text;
  	c_dict=root[company];
	var c_list=c_dict[qtag];
	if (c_list!=null) {
		//alert("c_list loaded properly");
	}
	loadQuestions(c_list);
	});
}
else {
	d3.json(questions2, function(error, list) {
  	if (error) return alert("error loading cluster 2 file");
	var company1se = document.getElementById('company1s');
	var company2se = document.getElementById('company2s');
	var company1 = company1se.options[company1se.selectedIndex].text;
	var company2 = company2se.options[company2se.selectedIndex].text;
	var qtage = document.getElementById('qtags');
	var qtag=qtage.options[qtage.selectedIndex].text;
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



