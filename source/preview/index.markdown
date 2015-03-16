---
layout: page
title: "Proposal for a more agile DO-178"
date: 2015-03-17 00:27
comments: true
sharing: true
footer: true
---

When looking at software development methodologies, there is in my mind a spectrum that looks something as follows:

{% img center /images/Development_spectrum.png 600 %}

So whats wrong with the extremes of waterfall or agile development, especially concerning safety critical products? Well I think Dilbert may have some advice to share here. Waterfall development suffers from the following:

{% img center /images/dilbert_2001_04_14.png 600 %}

This way, alot of unnecesarry requirements gets specified, because the client is scared that if he doesn't name every possible use case his product could get used for, he won't have another chance. The result is bloat, cost increases and increases in the product complexity, not great for safety critical products.

Ok, so agile should be perfect then:

{% img center /images/dilbert_1997_05_09.gif 600 %}

Nope, agile struggles to guarantee that the product is safe. Agile tries to shorten the feedback cycle, "fail fast" or "move fast and break things". Well when you are developing software for an aircraft, you can't exactly crash an airplane every time you release and then quickly fix the bug, even if you do it fast...

Ok, so up to now most DO-178 development was done with waterfall methodologies, but what might an agile DO-178 development process look like?

The deliverables for DO-178 looks as follows, and is usually produced at the following stages with waterfall development:

**Organisational:**<br/>
(These can be re-used accross multiple projects, if the projects are similar enough off course)

- SCM (Software configuration management plan)
- SQAP (Software quality assurance plan)
- SRS (Software requirements standards)
- SDS (Software design standards)
- SCS (Software code standards)
- SVP (Software verification plan)

**At the start of a project:**

- PSAC (Plan for software aspects of certification)
- SDP (Software development plan)
- SRD (Software requirements data)
- DD (Design description)

**During development:**

- Source code
- Object code
- SVCP (Software verification Cases and Procedures)
- Problem reports
- SQA (Software Quality Assurance Records)

**At the end of a project:**

- SVR (Software Verification Results)
- SECI (Software Life Cycle Environment Configuration Index)
- SCI (Software Configuration Index)
- SCMR (Software Configuration Management Records)
- SAS (Software Accomplishment Summary)

The problem here is that a lot of the deliverables are generated at the start of a project, before the lessons has been learned. And a lot of the deliverables are generated at the end of a project, not keeping pace with the development of the software, and as such represent a signifant source of costs, as these have to be produced and verified manually. 

The organisational deliverables is not my concern here, as once these has been generated they can be re-used accross multiple projects. But let's see if we can get some of the project specific deliverables be generated and verified continuously during development using the following:

<h3>Scrum</h3>
During sprint planning and review sessions, we can generate the DD's (Design descriptions) and SRD's (Software Requirements Data) continuously. It will look something like this...

{% img center /images/DO178_scrum.png 600 %}

<h3>Continuous integration (CI) and Continuous deployment (CD)</h3>
CI and CD can be used to generate the SCI and SCMR deliverables. In effect the CI server is the SECI and SCI. TODO 

{% img center /images/testing_pyramid.png 600 %}

<h3>Test driven development</h3>
Test driven development can be used to generate the Software Verification Cases and Procedures (SVCP's) and Software Verification Results (SVR's). High level requirements will be developed and tested with feature driven development, and unit tests will be used to develop and test low level requirements. But not all unit tests are really low level requirements, for instance testing if a function can handle null pointer parameters. As such we will mark which unit tests are indeed low level requirements in the unit testing code itself. 

This means an agile setup might look as follows:

{% img center /images/agile_setup.png 600 %}

And what will the workflow differences look like between a waterfall and agile DO-178 project? The following represents a very simplified project workflow, and may undoubtly differ from other DO-178 projects.



Going back to the DO-178B specification, it lists as an appendix the requirements for the deliverables. The purpose of an agile process would be then to automate the verification of as many of these requirements in order to speed up the certification and re-certification of the product. The difference between how a waterfall or agile work flow satisfies these requirements then looks as follows:

<html>
<style>
#TBody,#Heading
{
text-align:left;
background-color:lightgrey;
border:solid 1px black;
padding:2px;
height:100%
}

#TChange
{
text-align:left;
background-color:red;
border:solid 1px black;
padding:2px;
height:100%
}
</style>
</html>

Table A-1: Software planning process

<table border="1" style="height:100%; width: 100%;">
  <tr>
	<td><div id="Heading"></div></td>
    <td><div id="Heading">Objective</div></td>
    <td><div id="Heading">Output</div></td>
	<td><div id="Heading">Agile strategy</div></td>
  </tr>

  <tr>
	<td><div id="TBody">1</div></td>
    <td><div id="TBody">Software development and integral processes activities are defined</div></td>
    <td rowspan="4"><div id="TBody">Plan for Software Aspects of Certification<br/><br/>
									Software Development Plan<br/><br/>
									Software Verification Plan<br/><br/>
									Software Configuration Management Plan<br/><br/>
									Software Quality Assurance Plan</div></td> 
	<td><div id="TBody">doc</div></td>
  </tr>

  <tr>
	<td><div id="TBody">2</div></td>
    <td><div id="TBody">Transition criteria, inter-relationships and sequencing among processes are defined</div></td> 
	<td><div id="TBody">doc</div></td>
  </tr>  

  <tr>
	<td><div id="TBody">3</div></td>
    <td><div id="TBody">Software lifecycle environment is defined</div></td> 
	<td><div id="TBody">doc</div></td>
  </tr> 

  <tr>
	<td><div id="TBody">4</div></td>
    <td><div id="TBody">Additional considerations are addressed</div></td> 
	<td><div id="TBody">doc</div></td>
  </tr> 

  <tr>
	<td><div id="TBody">5</div></td>
    <td><div id="TBody">Software development standards are defined</div></td> 
	<td><div id="TBody">SW Requirements standards<br/><br/>
						SW Design Standards<br/><br/>
						SW Code Standards</div></td>
	<td><div id="TBody">doc</div></td>
  </tr>

  <tr>
	<td><div id="TBody">6</div></td>
    <td><div id="TBody">Software plans comply with this document</div></td> 
	<td><div id="TBody">Software Quality Assurance Records<br/><br/>
						Software verification results</div></td>
	<td><div id="TBody">doc</div></td>
  </tr>

  <tr>
	<td><div id="TBody">7</div></td>
    <td><div id="TBody">Software plans are coordinated</div></td> 
	<td><div id="TBody">Software Quality Assurance Records<br/><br/>
						Software verification results</div></td>
	<td><div id="TBody">doc</div></td>
  </tr>
</table>
<br/>

Table A-2: Software Development processes

<table border="1" style="height:100px; width: 100%;">
  <tr>
	<td><div id="Heading"></div></td>
    <td><div id="Heading">Objective</div></td>
    <td><div id="Heading">Output</div></td>
	<td><div id="Heading">Agile strategy</div></td>
  </tr>

  <tr>
	<td><div id="TBody">1</div></td>
    <td><div id="TBody">High-level requirements are developed</div></td>
    <td><div id="TBody">Software Requirements Data</div></td> 
	<td><div id="TBody">doc</div></td>
  </tr>

  <tr>
	<td><div id="TBody">2</div></td>
    <td><div id="TBody">Derived high-level requirements are defined</div></td>
	<td><div id="TBody">Software Requirements Data</div></td> 
	<td><div id="TBody">doc</div></td>
  </tr>  

  <tr>
	<td><div id="TBody">3</div></td>
    <td><div id="TBody">Software architecture is developed</div></td> 
	<td><div id="TBody">Design description</div></td>	
	<td><div id="TBody">doc</div></td>
  </tr> 

  <tr>
	<td><div id="TBody">4</div></td>
    <td><div id="TBody">Low level requirements are developed</div></td> 
	<td><div id="TBody">Design description</div></td>
	<td><div id="TBody">doc</div></td>
  </tr> 

  <tr>
	<td><div id="TBody">5</div></td>
    <td><div id="TBody">Derived low-level requirements are defined</div></td> 
	<td><div id="TBody">Design description</div></td>
	<td><div id="TChange">doc</div></td>
  </tr>

  <tr>
	<td><div id="TBody">6</div></td>
    <td><div id="TBody">Source code is developed</div></td> 
	<td><div id="TBody">Source code</div></td>
	<td><div id="TBody">doc</div></td>
  </tr>

  <tr>
	<td><div id="TBody">7</div></td>
    <td><div id="TBody">Executable Object Code is produced and integrated into the target computer</div></td> 
	<td><div id="TBody">Executable object code</div></td>
	<td><div id="TBody">doc</div></td>
  </tr>
</table>
<br/>

Table A-3: Verification of Outputs of Software Requirements Process

<table border="1" style="height:100px; width: 100%;">
  <tr>
	<td><div id="Heading"></div></td>
    <td><div id="Heading">Objective</div></td>
    <td><div id="Heading">Output</div></td>
	<td><div id="Heading">Agile strategy</div></td>
  </tr>

  <tr>
	<td><div id="TBody">1</div></td>
    <td><div id="TBody">Software high-level requirements comply with system requirements</div></td>
    <td><div id="TBody">Software Verification Results</div></td> 
	<td><div id="TBody">doc</div></td>
  </tr>

  <tr>
	<td><div id="TBody">2</div></td>
    <td><div id="TBody">High level requirements are accurate and consistent</div></td>
	<td><div id="TBody">Software Verification Results</div></td> 
	<td><div id="TBody">doc</div></td>
  </tr>  

  <tr>
	<td><div id="TBody">3</div></td>
    <td><div id="TBody">High level requirements are compatible with target computer</div></td> 
	<td><div id="TBody">Software Verification Results</div></td>	
	<td><div id="TBody">doc</div></td>
  </tr> 

  <tr>
	<td><div id="TBody">4</div></td>
    <td><div id="TBody">High level requirements are verifiable</div></td> 
	<td><div id="TBody">Software Verification Results</div></td>
	<td><div id="TBody">doc</div></td>
  </tr> 

  <tr>
	<td><div id="TBody">5</div></td>
    <td><div id="TBody">High level requirements conform to standards</div></td> 
	<td><div id="TBody">Software Verification Results</div></td>
	<td><div id="TChange">doc</div></td>
  </tr>

  <tr>
	<td><div id="TBody">6</div></td>
    <td><div id="TBody">High level requirements are traceable to system requirements</div></td> 
	<td><div id="TBody">Software Verification Results</div></td>
	<td><div id="TBody">doc</div></td>
  </tr>

  <tr>
	<td><div id="TBody">7</div></td>
    <td><div id="TBody">Algorithms are accurate</div></td> 
	<td><div id="TBody">Software Verification Results</div></td>
	<td><div id="TBody">doc</div></td>
  </tr>
</table>
<br/>

Table A-4: Verification of Outputs of Software Design Process

<table border="1" style="height:100px; width: 100%;">
  <tr>
	<td><div id="Heading"></div></td>
    <td><div id="Heading">Objective</div></td>
    <td><div id="Heading">Output</div></td>
	<td><div id="Heading">Agile strategy</div></td>
  </tr>

  <tr>
	<td><div id="TBody">1</div></td>
    <td><div id="TBody">Low level requirements comply with high level requirements</div></td>
    <td><div id="TBody">Software Verification Results</div></td> 
	<td><div id="TBody">doc</div></td>
  </tr>

  <tr>
	<td><div id="TBody">2</div></td>
    <td><div id="TBody">Low level requirements are accurate and consistent</div></td>
	<td><div id="TBody">Software Verification Results</div></td> 
	<td><div id="TBody">doc</div></td>
  </tr>  

  <tr>
	<td><div id="TBody">3</div></td>
    <td><div id="TBody">Low level requirements are compatible with target computer</div></td> 
	<td><div id="TBody">Software Verification Results</div></td>	
	<td><div id="TBody">doc</div></td>
  </tr> 

  <tr>
	<td><div id="TBody">4</div></td>
    <td><div id="TBody">Low level requirements are verifiable</div></td> 
	<td><div id="TBody">Software Verification Results</div></td>
	<td><div id="TBody">doc</div></td>
  </tr> 

  <tr>
	<td><div id="TBody">5</div></td>
    <td><div id="TBody">Low level requirements conform to standards</div></td> 
	<td><div id="TBody">Software Verification Results</div></td>
	<td><div id="TChange">doc</div></td>
  </tr>

  <tr>
	<td><div id="TBody">6</div></td>
    <td><div id="TBody">Low level requirements are traceable to High level requirements</div></td> 
	<td><div id="TBody">Software Verification Results</div></td>
	<td><div id="TBody">doc</div></td>
  </tr>

  <tr>
	<td><div id="TBody">7</div></td>
    <td><div id="TBody">Algorithms are accurate</div></td> 
	<td><div id="TBody">Software Verification Results</div></td>
	<td><div id="TBody">doc</div></td>
  </tr>

  <tr>
	<td><div id="TBody">8</div></td>
    <td><div id="TBody">Software architecture is compatible with high level requirements</div></td> 
	<td><div id="TBody">Software Verification Results</div></td>
	<td><div id="TBody">doc</div></td>
  </tr>

  <tr>
	<td><div id="TBody">9</div></td>
    <td><div id="TBody">Software architecture is consistent</div></td> 
	<td><div id="TBody">Software Verification Results</div></td>
	<td><div id="TBody">doc</div></td>
  </tr>

  <tr>
	<td><div id="TBody">10</div></td>
    <td><div id="TBody">Software architecture is compatible with target computer</div></td> 
	<td><div id="TBody">Software Verification Results</div></td>
	<td><div id="TBody">doc</div></td>
  </tr>

  <tr>
	<td><div id="TBody">11</div></td>
    <td><div id="TBody">Software architecture is verifiable</div></td> 
	<td><div id="TBody">Software Verification Results</div></td>
	<td><div id="TBody">doc</div></td>
  </tr>

  <tr>
	<td><div id="TBody">12</div></td>
    <td><div id="TBody">Software architecture conforms to standards</div></td> 
	<td><div id="TBody">Software Verification Results</div></td>
	<td><div id="TBody">doc</div></td>
  </tr>

  <tr>
	<td><div id="TBody">13</div></td>
    <td><div id="TBody">Software partitioning integrity is confirmed</div></td> 
	<td><div id="TBody">Software Verification Results</div></td>
	<td><div id="TBody">doc</div></td>
  </tr>
</table>
<br/>

Table A-5: Verification of Outputs of Software Coding and Integration Process

<table border="1" style="height:100px; width: 100%;">
  <tr>
	<td><div id="Heading"></div></td>
    <td><div id="Heading">Objective</div></td>
    <td><div id="Heading">Output</div></td>
	<td><div id="Heading">Agile strategy</div></td>
  </tr>

  <tr>
	<td><div id="TBody">1</div></td>
    <td><div id="TBody">Source code complies with low level requirements</div></td>
    <td><div id="TBody">Software Verification Results</div></td> 
	<td><div id="TBody">doc</div></td>
  </tr>

  <tr>
	<td><div id="TBody">2</div></td>
    <td><div id="TBody">Source code complies with software architecture</div></td>
	<td><div id="TBody">Software Verification Results</div></td> 
	<td><div id="TBody">doc</div></td>
  </tr>  

  <tr>
	<td><div id="TBody">3</div></td>
    <td><div id="TBody">Source code is verifiable</div></td> 
	<td><div id="TBody">Software Verification Results</div></td>	
	<td><div id="TBody">doc</div></td>
  </tr> 

  <tr>
	<td><div id="TBody">4</div></td>
    <td><div id="TBody">Source code confirms to standards</div></td> 
	<td><div id="TBody">Software Verification Results</div></td>
	<td><div id="TBody">doc</div></td>
  </tr> 

  <tr>
	<td><div id="TBody">5</div></td>
    <td><div id="TBody">Source code is traceable to low level requirements</div></td> 
	<td><div id="TBody">Software Verification Results</div></td>
	<td><div id="TChange">doc</div></td>
  </tr>

  <tr>
	<td><div id="TBody">6</div></td>
    <td><div id="TBody">Source code is accurate and consistent</div></td> 
	<td><div id="TBody">Software Verification Results</div></td>
	<td><div id="TBody">doc</div></td>
  </tr>

  <tr>
	<td><div id="TBody">7</div></td>
    <td><div id="TBody">Output of software integration process is complete and correct</div></td> 
	<td><div id="TBody">Software Verification Results</div></td>
	<td><div id="TBody">doc</div></td>
  </tr>
</table>
<br/>

Table A-6: Testing of Outputs of Integration Process

<table border="1" style="height:100px; width: 100%;">
  <tr>
	<td><div id="Heading"></div></td>
    <td><div id="Heading">Objective</div></td>
    <td><div id="Heading">Output</div></td>
	<td><div id="Heading">Agile strategy</div></td>
  </tr>

  <tr>
	<td><div id="TBody">1</div></td>
    <td><div id="TBody">Executable object code complies with high level requirements</div></td>
    <td><div id="TBody">Software Verification Cases and Procedures<br/><br/>
						Software Verification Results</div></td> 
	<td><div id="TBody">doc</div></td>
  </tr>

  <tr>
	<td><div id="TBody">2</div></td>
    <td><div id="TBody">Executable object code is robust with high level requirements</div></td>
	<td><div id="TBody">Software Verification Cases and Procedures<br/><br/>
						Software Verification Results</div></td> 
	<td><div id="TBody">doc</div></td>
  </tr>  

  <tr>
	<td><div id="TBody">3</div></td>
    <td><div id="TBody">Executable object code complies with low level requirements</div></td> 
	<td><div id="TBody">Software Verification Cases and Procedures<br/><br/>
						Software Verification Results</div></td>	
	<td><div id="TBody">doc</div></td>
  </tr> 

  <tr>
	<td><div id="TBody">4</div></td>
    <td><div id="TBody">Executable object code is robust with low level requirements</div></td> 
	<td><div id="TBody">Software Verification Cases and Procedures<br/><br/>
						Software Verification Results</div></td>
	<td><div id="TBody">doc</div></td>
  </tr> 

  <tr>
	<td><div id="TBody">5</div></td>
    <td><div id="TBody">Executable object code is compatible with target computer</div></td> 
	<td><div id="TBody">Software Verification Cases and Procedures<br/><br/>
						Software Verification Results</div></td>
	<td><div id="TChange">doc</div></td>
  </tr>
</table>
<br/>

Table A-7: Verification of Verification Process Results

<table border="1" style="height:100px; width: 100%;">
  <tr>
	<td><div id="Heading"></div></td>
    <td><div id="Heading">Objective</div></td>
    <td><div id="Heading">Output</div></td>
	<td><div id="Heading">Agile strategy</div></td>
  </tr>

  <tr>
	<td><div id="TBody">1</div></td>
    <td><div id="TBody">Test procedures are correct</div></td>
    <td><div id="TBody">Software Verification Cases and Procedures</div></td> 
	<td><div id="TBody">doc</div></td>
  </tr>

  <tr>
	<td><div id="TBody">2</div></td>
    <td><div id="TBody">Test results are correct and disrepancies explained </div></td>
	<td><div id="TBody">Software Verification Results</div></td> 
	<td><div id="TBody">doc</div></td>
  </tr>  

  <tr>
	<td><div id="TBody">3</div></td>
    <td><div id="TBody">Test coverage of high level requirements is achieved</div></td> 
	<td><div id="TBody">Software Verification Results</div></td>	
	<td><div id="TBody">doc</div></td>
  </tr> 

  <tr>
	<td><div id="TBody">4</div></td>
    <td><div id="TBody">Test coverage of low level requirements is achieved</div></td> 
	<td><div id="TBody">Software Verification Results</div></td>
	<td><div id="TBody">doc</div></td>
  </tr> 

  <tr>
	<td><div id="TBody">5</div></td>
    <td><div id="TBody">Test coverage of software structure (modified condition / decision) is achieved</div></td> 
	<td><div id="TBody">Software Verification Results</div></td>
	<td><div id="TChange">doc</div></td>
  </tr>

  <tr>
	<td><div id="TBody">6</div></td>
    <td><div id="TBody">Test coverage of software structure (decision coverage) is achieved</div></td> 
	<td><div id="TBody">Software Verification Results</div></td>
	<td><div id="TBody">doc</div></td>
  </tr>

  <tr>
	<td><div id="TBody">7</div></td>
    <td><div id="TBody">Test coverage of software structure (statement coverage) is achieved</div></td> 
	<td><div id="TBody">Software Verification Results</div></td>
	<td><div id="TBody">doc</div></td>
  </tr>

  <tr>
	<td><div id="TBody">8</div></td>
    <td><div id="TBody">Test coverage of software structure (data coupling and control coupling) is achieved</div></td> 
	<td><div id="TBody">Software Verification Results</div></td>
	<td><div id="TBody">doc</div></td>
  </tr>
</table>
<br/>

Table A-8: Software Configuration Management Process 

<table border="1" style="height:100px; width: 100%;">
  <tr>
	<td><div id="Heading"></div></td>
    <td><div id="Heading">Objective</div></td>
    <td><div id="Heading">Output</div></td>
	<td><div id="Heading">Agile strategy</div></td>
  </tr>

  <tr>
	<td><div id="TBody">1</div></td>
    <td><div id="TBody">Configuration items are identified</div></td>
    <td><div id="TBody">SCM Records</div></td> 
	<td><div id="TBody">doc</div></td>
  </tr>

  <tr>
	<td><div id="TBody">2</div></td>
    <td><div id="TBody">Baselines and traceability are established</div></td>
	<td><div id="TBody">Software Configuration index <br/><br/>
						SCM Records</div></td> 
	<td><div id="TBody">doc</div></td>
  </tr>  

  <tr>
	<td><div id="TBody">3</div></td>
    <td><div id="TBody">Problem reporting, change control, change review, and configuration status accounting are established</div></td> 
	<td><div id="TBody">Problem reports<br/><br/>
						SCM Records</div></td>	
	<td><div id="TBody">doc</div></td>
  </tr> 

  <tr>
	<td><div id="TBody">4</div></td>
    <td><div id="TBody">Archive, retrieval, and release are established</div></td> 
	<td><div id="TBody">SCM Records</div></td>
	<td><div id="TBody">doc</div></td>
  </tr> 

  <tr>
	<td><div id="TBody">5</div></td>
    <td><div id="TBody">Software load control is established</div></td> 
	<td><div id="TBody">SCM Records</div></td>
	<td><div id="TChange">doc</div></td>
  </tr>

  <tr>
	<td><div id="TBody">6</div></td>
    <td><div id="TBody">Software life cycle environment control is established</div></td> 
	<td><div id="TBody">Software Life Cycle Environment Configuration Index<br/><br/>
						SCM Records</div></td>
	<td><div id="TBody">doc</div></td>
  </tr>
</table>
<br/>

Table A-9: Software Quality Assurance Process 

<table border="1" style="height:100px; width: 100%;">
  <tr>
	<td><div id="Heading"></div></td>
    <td><div id="Heading">Objective</div></td>
    <td><div id="Heading">Output</div></td>
	<td><div id="Heading">Agile strategy</div></td>
  </tr>

  <tr>
	<td><div id="TBody">1</div></td>
    <td><div id="TBody">Assurance is obtained that software development and integral processes comply with approved software plans and standards</div></td>
    <td><div id="TBody">Software Quality Assurance Records</div></td> 
	<td><div id="TBody">doc</div></td>
  </tr>

  <tr>
	<td><div id="TBody">2</div></td>
    <td><div id="TBody">Assurance is obtained that transition criteria for the software life cycle processes are satisfied</div></td>
	<td><div id="TBody">Software Quality Assurance Records</div></td> 
	<td><div id="TBody">doc</div></td>
  </tr>  

  <tr>
	<td><div id="TBody">3</div></td>
    <td><div id="TBody">Software conformity review is conducted</div></td> 
	<td><div id="TBody">Software Quality Assurance Records</div></td>	
	<td><div id="TBody">doc</div></td>
  </tr> 
</table>
<br/>

Table A-10: Certification Liaison Process 

<table border="1" style="height:100px; width: 100%;">
  <tr>
	<td><div id="Heading"></div></td>
    <td><div id="Heading">Objective</div></td>
    <td><div id="Heading">Output</div></td>
	<td><div id="Heading">Agile strategy</div></td>
  </tr>

  <tr>
	<td><div id="TBody">1</div></td>
    <td><div id="TBody">Communication and understanding between the applicant and the certification authority is established</div></td>
    <td><div id="TBody">Plan for software aspects of certification</div></td> 
	<td><div id="TBody">doc</div></td>
  </tr>

  <tr>
	<td><div id="TBody">2</div></td>
    <td><div id="TBody">The means of compliance is proposed and agreement with the plan Plan for Software Aspects of Certification is obtained</div></td>
	<td><div id="TBody">Plan for software aspects of certification</div></td> 
	<td><div id="TBody">doc</div></td>
  </tr>  

  <tr>
	<td><div id="TBody">3</div></td>
    <td><div id="TBody">Compliance substantiation is provided</div></td> 
	<td><div id="TBody">Software Accomplishment Summary<br/><br/>
						Software Configuration Index</div></td>	
	<td><div id="TBody">doc</div></td>
  </tr> 
</table>
<br/>

So there you have it, a proposal on what a more agile DO-178 development process might look like. The question now is, will this pass certification, and can this agile process deliver software of at least the same robustness / quality as a waterfall process delivers. For this question, I will be guiding two three-man student groups to complete the same software project, one group following the waterfall model and another group following the agile model. More on that in the next post.

If I have missed anything or you would like to make a suggestion, kindly do so at the discussion on [HN](https://news.ycombinator.com/item?id=8937549) and [reddit](http://www.reddit.com/r/programming/comments/2tg71e/do178b_crash_course/). Comments and suggestions are very welcome.

If you are currently; or in the past have worked on DO-178 projects, it would be appreciated if you would be so kind as to [take part in a quick survey](https://www.surveymonkey.com/s/SV9KX7M) about the state of DO-178 development. I will release the results of this survey shortly. Thank you for everyone who has completed the survey already.