---
layout: post
title: "A more Agile DO-178"
date: 2015-04-08 23:02:59 +0200
comments: true
categories: 
---

When looking at software development methodologies, there is in my mind a spectrum that looks something as follows:

{% img center /images/Development_spectrum.png 600 %}


So what's wrong with the extremes of waterfall or agile development, especially concerning safety critical products? Well I think Dilbert may have some advice to share here. Waterfall development typically suffers from the following:

{% img center /images/dilbert_2001_04_14.png 600 %}
<center><small>DILBERT © 2001 Scott Adams. Used By permission of UNIVERSAL UCLICK. All rights reserved.</small></center><br/>


With waterfall development, a lot of unnecessary requirements gets specified, because the client is scared that if he doesn't name every possible use case his product could get used for, he won't have another chance. The result is bloat, increased costs and increases in the product complexity, not great for safety critical products.

Ok, so agile should be perfect then?

{% img center /images/dilbert_1997_05_09.gif 600 %}
<center><small>DILBERT © 1997 Scott Adams. Used By permission of UNIVERSAL UCLICK. All rights reserved.</small></center><br/>


Nope, agile struggles to guarantee that the product is safe. Agile tries to shorten the feedback cycle, "fail fast" or "move fast and break things". Well when you are developing software for an aircraft, you can't exactly crash an airplane every time you release and then quickly fix the bug, even if you do it fast...

Ok, so up to now most DO-178 development was done with waterfall methodologies, but what might a more agile DO-178 development process look like?

To answer this question, we have to look at the deliverables required for DO-178 certification, and at what stages of the waterfall development model they are typically produced:

**Organisational:**<br/>
(These can be re-used across multiple projects, if the projects are similar enough off course)

- Software configuration management plan (SCM)
- Software quality assurance plan (SQA)
- Software requirements standards (SRS)
- Software design standards (SDS)
- Software code standards (SCS)
- Software verification plan (SVP)

**At the start of a project - Specification phase:**

- Plan for software aspects of certification (PSAC)
- Software development plan (SDP)
- Software requirements data (SRD)
- Design description (DD)

**During development - Implementation phase:**

- Source code
- Object code
- Software verification Cases and Procedures (SVCP)
- Problem reports
- Software Quality Assurance Records (SQA)
- Software Configuration Management Records (SCMR)

**At the end of a project - Testing and verification phase:**

- Software Verification Results (SVR)
- Software Life Cycle Environment Configuration Index (SECI)
- Software Configuration Index (SCI)
- Software Accomplishment Summary (SAS)

The problem here is that a lot of the deliverables are generated at the start of a project, before the lessons have been learned. And a lot of the deliverables are generated at the end of a project, not keeping pace with the development of the software, and as such represent a significant source of costs, as these have to be produced and verified manually. 

Most of these deliverables also usually takes the form of documentation, with the exception of the source code and object code. DO-178 does not specifically state that the outputs have to be in the form of documentation, and where possible we will try to replace traditionally labour intensive documentation with other artefacts, saving us effort and costs. Off course we must prove that there is no reduction in the reliability of the final product when making these changes.  

The organisational deliverables is not my concern here, as once these have been generated they can be re-used across multiple projects. But let's see if we can get some of the project specific deliverables be generated and verified continuously and automatically during development using the following:

<h3>Scrum</h3>
During sprint planning and review sessions, we can review and update the Design Description (DD) document detailing the software architecture. At the end of a sprint, the implemented user stories will form the Software Requirements Data (SRD's). It will look something like this...

{% img center /images/DO178_scrum.png 600 %}

During sprint planning we ensure that the user stories i.e. the high level requirements we are planning to implement is consistent with previous implemented requirements.
During sprint review we update the requirements with the implemented user stories, and ensure the created functional tests and unit tests i.e. the low level requirements are consistent with the high level requirements (user stories).

This turns the traditional waterfall model on it's head. How can you write code and generate the requirements only afterwards? Well a lot of times, you only realise what the true requirements are when you are writing the code, so we only set the requirements in stone once we are sure. We still generate user stories as possible requirements before writing code.

<h3>Continuous integration (CI) and Continuous deployment (CD)</h3>
The CI and CD servers themselves are effectively the Software Life Cycle Environment Configuration Index (SECI), Software Configuration Index (SCI) and parts of the Sofware Configuration Management Records (SCMR) deliverables. For this to be possible, the CI server must have a copy of the version control database when duplicated for certification.   

This means an agile setup might look as follows:

{% img center /images/agile_setup.png 600 %}

If all the tests pass, the CI / CD will autogenerate a snapshot of itself (VM's or some other duplication means) and the version control database to serve as the SECI and SCI. It will also generate reports of the tests run and their results to serve as the SVP and SVR's, and generate reports that can serve as SCMR items (This is baselines, commit histories etc.). This is off course highly idealistic and represents no small amount of additional work, but the purpose here is to show that these required deliverables of DO-178 is fairly repetative and thus highly automatable. 

<h3>Test driven development</h3>
Test driven development can be used to generate the large parts of the Software Verification Cases and Procedures (SVCP's) and Software Verification Results (SVR's). High level requirements will be developed and tested with feature driven development, and unit tests will be used to develop and test low level requirements. But not all unit tests are really low level requirements, for instance testing if a function can handle null pointer parameters. As such we will mark which unit tests are indeed low level requirements in the unit testing code itself.  

The relationship between the Continuous integration (CI) server and the Continuous deployment (CD) server is detailed in the popular test pyramid developed by Mike Cohn, where the CI is responsible for making sure the source code compiles at all times, and passes all unit tests, and the CD is responsible for making sure the automated functional tests pass at all times. One would expect to develop a lot more unit tests than functional tests, thereby limiting (but not eliminating) the need for expensive manual testing.

{% img center /images/testing_pyramid.png 600 %}

And what will the workflow differences look like between a waterfall and agile DO-178 project? The following represents a very simplified project workflow, but will hopefully give you an idea.

_Every blue item represents a stage gate, that has to be satisfied before the team can continue on to the next set of items_

{% img center /images/agileWaterfallTeamActivities.png 600 %}

*Sprint review includes a retrospective, code review, functional and unit tests review.

Going back to the DO-178 specification, it lists as an appendix the requirements for the deliverables. The purpose of an agile process would be then to automate the verification of as many of these requirements in order to speed up the certification and re-certification of the product. The difference between how a waterfall or agile work flow satisfies these requirements then looks as follows (DO-178C wording used):

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
    <td><div id="TBody">The activities of the software life cycle processes are defined.</div></td>
    <td rowspan="4"><div id="TBody">Plan for Software Aspects of Certification<br/><br/>
                                    Software Development Plan<br/><br/>
                                    Software Verification Plan<br/><br/>
                                    Software Configuration Management Plan<br/><br/>
                                    Software Quality Assurance Plan</div></td> 
    <td><div id="TBody">An agile process is defined.</div></td>
  </tr>

  <tr>
    <td><div id="TBody">2</div></td>
    <td><div id="TBody">The software life cycle(s), including the inter-relationships between the processes, their sequencing, feedback mechanisms, and transition criteria, is defined.</div></td> 
    <td><div id="TBody">An agile process is defined.</div></td>
  </tr>  

  <tr>
    <td><div id="TBody">3</div></td>
    <td><div id="TBody">Software life cycle environment is selected and defined.</div></td> 
    <td><div id="TBody">The CI server is defined as the software lifecycle environment as a final deliverable.</div></td>
  </tr> 

  <tr>
    <td><div id="TBody">4</div></td>
    <td><div id="TBody">Additional considerations are addressed</div></td> 
    <td><div id="TBody">No difference.</div></td>
  </tr> 

  <tr>
    <td><div id="TBody">5</div></td>
    <td><div id="TBody">Software development standards are defined</div></td> 
    <td><div id="TBody">SW Requirements standards<br/><br/>
                        SW Design Standards<br/><br/>
                        SW Code Standards</div></td>
    <td><div id="TBody">No difference.</div></td>
  </tr>

  <tr>
    <td><div id="TBody">6</div></td>
    <td><div id="TBody">Software plans comply with this document</div></td> 
    <td><div id="TBody">Software Quality Assurance Records<br/><br/>
                        Software verification results</div></td>
    <td><div id="TBody">The SVR's will now be automatically generated by the unit tests, and the CD server, with a small section still generated manually with manual testing.</div></td>
  </tr>

  <tr>
    <td><div id="TBody">7</div></td>
    <td><div id="TBody">Development and revision of software plans are coordinated.</div></td> 
    <td><div id="TBody">Software Quality Assurance Records<br/><br/>
                        Software verification results.</div></td>
    <td><div id="TBody">No difference</div></td>
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
    <td><div id="TBody">At the end of each scrum, the implemented user stories will generate the high level requirements section in the SRD.</div></td>
  </tr>

  <tr>
    <td><div id="TBody">2</div></td>
    <td><div id="TBody">Derived high-level requirements are defined and provided to the system processes, including the system safety assessment process.</div></td>
    <td><div id="TBody">Software Requirements Data</div></td> 
    <td><div id="TBody">At the end of each scrum, the implemented derived user stories will generate the high level requirements section in the SRD. There is a problem here, in that the system safety assesment process requires the high level requirements as input, and determines the DO-178 level required, but in an agile process the high level requirements are not defined at the beginning of a project.</div></td>
  </tr>  

  <tr>
    <td><div id="TBody">3</div></td>
    <td><div id="TBody">Software architecture is developed</div></td> 
    <td><div id="TBody">Design description</div></td>    
    <td><div id="TBody">At the beginning of each scrum, the software architecture is reviewed, at the end of each scrum the software architecture document (DD) is updated.</div></td>
  </tr> 

  <tr>
    <td><div id="TBody">4</div></td>
    <td><div id="TBody">Low level requirements are developed</div></td> 
    <td><div id="TBody">Design description</div></td>
    <td><div id="TBody">At the end of each scrum, the implemented unit tests marked as low level requirements will generate the low level requirements section in the DD.</div></td>
  </tr> 

  <tr>
    <td><div id="TBody">5</div></td>
    <td><div id="TBody">Derived low-level requirements are defined and provided to the system processes, including the system safety assessment process.</div></td> 
    <td><div id="TBody">Design description</div></td>
    <td><div id="TBody">At the end of each scrum, the implemented unit tests marked as low level requirements will generate the low level requirements section in the DD.</div></td>
  </tr>

  <tr>
    <td><div id="TBody">6</div></td>
    <td><div id="TBody">Source code is developed</div></td> 
    <td><div id="TBody">Source code</div></td>
    <td><div id="TBody">No difference.</div></td>
  </tr>

  <tr>
    <td><div id="TBody">7</div></td>
    <td><div id="TBody">Executable Object Code and Parameter Data Item Files, if any, are produced and loaded in the target computer.</div></td> 
    <td><div id="TBody">Executable object code</div></td>
    <td><div id="TBody">No difference.</div></td>
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
    <td><div id="TBody">High-level requirements comply with system requirements.</div></td>
    <td><div id="TBody">Software Verification Results</div></td> 
    <td><div id="TBody">At the beginning of each scrum, the suitability of the user stories to be implemented will be evaluated against the system requirements.</div></td>
  </tr>

  <tr>
    <td><div id="TBody">2</div></td>
    <td><div id="TBody">High level requirements are accurate and consistent</div></td>
    <td><div id="TBody">Software Verification Results</div></td> 
    <td><div id="TBody">User stories to be accurate and consistent.</div></td>
  </tr>  

  <tr>
    <td><div id="TBody">3</div></td>
    <td><div id="TBody">High level requirements are compatible with target computer</div></td> 
    <td><div id="TBody">Software Verification Results</div></td>    
    <td><div id="TBody">User stories verified with continuous deployment and functional tests.</div></td>
  </tr> 

  <tr>
    <td><div id="TBody">4</div></td>
    <td><div id="TBody">High level requirements are verifiable</div></td> 
    <td><div id="TBody">Software Verification Results</div></td>
    <td><div id="TBody">User stories verified with continuous deployment and functional tests.</div></td>
  </tr> 

  <tr>
    <td><div id="TBody">5</div></td>
    <td><div id="TBody">High level requirements conform to standards</div></td> 
    <td><div id="TBody">Software Verification Results</div></td>
    <td><div id="TBody">User stories to conform to standards.</div></td>
  </tr>

  <tr>
    <td><div id="TBody">6</div></td>
    <td><div id="TBody">High level requirements are traceable to system requirements</div></td> 
    <td><div id="TBody">Software Verification Results</div></td>
    <td><div id="TBody">No difference.</div></td>
  </tr>

  <tr>
    <td><div id="TBody">7</div></td>
    <td><div id="TBody">Algorithms are accurate</div></td> 
    <td><div id="TBody">Software Verification Results</div></td>
    <td><div id="TBody">No difference.</div></td>
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
    <td><div id="TBody">Newly written unit tests marked as low level requirements will be annotated as to which high level requirement it is traced to and reviewed at every sprint.</div></td>
  </tr>

  <tr>
    <td><div id="TBody">2</div></td>
    <td><div id="TBody">Low level requirements are accurate and consistent</div></td>
    <td><div id="TBody">Software Verification Results</div></td> 
    <td><div id="TBody">Unit tests to be accurate and consistent.</div></td>
  </tr>  

  <tr>
    <td><div id="TBody">3</div></td>
    <td><div id="TBody">Low level requirements are compatible with target computer</div></td> 
    <td><div id="TBody">Software Verification Results</div></td>    
    <td><div id="TBody">Unit tests verified with continuous integration.</div></td>
  </tr> 

  <tr>
    <td><div id="TBody">4</div></td>
    <td><div id="TBody">Low level requirements are verifiable</div></td> 
    <td><div id="TBody">Software Verification Results</div></td>
    <td><div id="TBody">Unit tests verified with continuous integration.</div></td>
  </tr> 

  <tr>
    <td><div id="TBody">5</div></td>
    <td><div id="TBody">Low level requirements conform to standards</div></td> 
    <td><div id="TBody">Software Verification Results</div></td>
    <td><div id="TBody">Unit tests to conform to standards.</div></td>
  </tr>

  <tr>
    <td><div id="TBody">6</div></td>
    <td><div id="TBody">Low level requirements are traceable to High level requirements</div></td> 
    <td><div id="TBody">Software Verification Results</div></td>
    <td><div id="TBody">Unit tests marked as low level requirements will be annotated as to which high level requirement it is traced to.</div></td>
  </tr>

  <tr>
    <td><div id="TBody">7</div></td>
    <td><div id="TBody">Algorithms are accurate</div></td> 
    <td><div id="TBody">Software Verification Results</div></td>
    <td><div id="TBody">Accuracy can be verified with unit tests.</div></td>
  </tr>

  <tr>
    <td><div id="TBody">8</div></td>
    <td><div id="TBody">Software architecture is compatible with high level requirements</div></td> 
    <td><div id="TBody">Software Verification Results</div></td>
    <td><div id="TBody">Software architecture to be reviewed and updated with every sprint.</div></td>
  </tr>

  <tr>
    <td><div id="TBody">9</div></td>
    <td><div id="TBody">Software architecture is consistent</div></td> 
    <td><div id="TBody">Software Verification Results</div></td>
    <td><div id="TBody">Software architecture to be reviewed and updated with every sprint.</div></td>
  </tr>

  <tr>
    <td><div id="TBody">10</div></td>
    <td><div id="TBody">Software architecture is compatible with target computer</div></td> 
    <td><div id="TBody">Software Verification Results</div></td>
    <td><div id="TBody">Software architecture verified with continuous deployment and functional tests.</div></td>
  </tr>

  <tr>
    <td><div id="TBody">11</div></td>
    <td><div id="TBody">Software architecture is verifiable</div></td> 
    <td><div id="TBody">Software Verification Results</div></td>
    <td><div id="TBody">Software architecture verified with continuous deployment and functional tests.</div></td>
  </tr>

  <tr>
    <td><div id="TBody">12</div></td>
    <td><div id="TBody">Software architecture conforms to standards</div></td> 
    <td><div id="TBody">Software Verification Results</div></td>
    <td><div id="TBody">Software architecture to be reviewed and updated with every sprint.</div></td>
  </tr>

  <tr>
    <td><div id="TBody">13</div></td>
    <td><div id="TBody">Software partitioning integrity is confirmed</div></td> 
    <td><div id="TBody">Software Verification Results</div></td>
    <td><div id="TBody">Software partitioning integrity verified with continuous deployment and functional tests.</div></td>
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
    <td><div id="TBody">Verified with unit tests.</div></td>
  </tr>

  <tr>
    <td><div id="TBody">2</div></td>
    <td><div id="TBody">Source code complies with software architecture</div></td>
    <td><div id="TBody">Software Verification Results</div></td> 
    <td><div id="TBody">Can be confirmed with sprint code reviews or peer programming.</div></td>
  </tr>  

  <tr>
    <td><div id="TBody">3</div></td>
    <td><div id="TBody">Source code is verifiable</div></td> 
    <td><div id="TBody">Software Verification Results</div></td>    
    <td><div id="TBody">Verified with unit tests and functional tests.</div></td>
  </tr> 

  <tr>
    <td><div id="TBody">4</div></td>
    <td><div id="TBody">Source code conforms to standards</div></td> 
    <td><div id="TBody">Software Verification Results</div></td>
    <td><div id="TBody">Can be confirmed with sprint code reviews or peer programming.</div></td>
  </tr> 

  <tr>
    <td><div id="TBody">5</div></td>
    <td><div id="TBody">Source code is traceable to low level requirements</div></td> 
    <td><div id="TBody">Software Verification Results</div></td>
    <td><div id="TBody">Verified with continuous integration and unit tests.</div></td>
  </tr>

  <tr>
    <td><div id="TBody">6</div></td>
    <td><div id="TBody">Source code is accurate and consistent</div></td> 
    <td><div id="TBody">Software Verification Results</div></td>
    <td><div id="TBody">Can be confirmed with sprint code reviews or peer programming.</div></td>
  </tr>

  <tr>
    <td><div id="TBody">7</div></td>
    <td><div id="TBody">Output of software integration process is complete and correct</div></td> 
    <td><div id="TBody">Software Verification Results</div></td>
    <td><div id="TBody">Software integration process verified with continuous deployment and functional tests.</div></td>
  </tr>

  <tr>
    <td><div id="TBody">8</div></td>
    <td><div id="TBody">Parameter Data Item File is correct and complete</div></td> 
    <td><div id="TBody">Software Verification Cases and Procedures<br/><br/>
                        Software Verification Result<br/></div></td>
    <td><div id="TBody">Parameter Data Item File verified with continuous deployment and functional tests.</div></td>
  </tr>

  <tr>
    <td><div id="TBody">9</div></td>
    <td><div id="TBody">Verification of Parameter Data Item File is achieved.</div></td> 
    <td><div id="TBody">Software Verification Results</div></td>
    <td><div id="TBody">Parameter Data Item File verified with continuous deployment and functional tests.</div></td>
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
    <td><div id="TBody">User stories verified with continuous deployment and functional tests.</div></td>
  </tr>

  <tr>
    <td><div id="TBody">2</div></td>
    <td><div id="TBody">Executable object code is robust with high level requirements</div></td>
    <td><div id="TBody">Software Verification Cases and Procedures<br/><br/>
                        Software Verification Results</div></td> 
    <td><div id="TBody">User stories verified with continuous deployment and functional tests.</div></td>
  </tr>  

  <tr>
    <td><div id="TBody">3</div></td>
    <td><div id="TBody">Executable object code complies with low level requirements</div></td> 
    <td><div id="TBody">Software Verification Cases and Procedures<br/><br/>
                        Software Verification Results</div></td>    
    <td><div id="TBody">Verified with continuous integration and unit tests.</div></td>
  </tr> 

  <tr>
    <td><div id="TBody">4</div></td>
    <td><div id="TBody">Executable object code is robust with low level requirements</div></td> 
    <td><div id="TBody">Software Verification Cases and Procedures<br/><br/>
                        Software Verification Results</div></td>
    <td><div id="TBody">Verified with continuous integration and unit tests.</div></td>
  </tr> 

  <tr>
    <td><div id="TBody">5</div></td>
    <td><div id="TBody">Executable object code is compatible with target computer</div></td> 
    <td><div id="TBody">Software Verification Cases and Procedures<br/><br/>
                        Software Verification Results</div></td>
    <td><div id="TBody">User stories verified with continuous deployment and functional tests.</div></td>
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
    <td><div id="TBody">Sprint review of unit tests and functional tests</div></td>
  </tr>

  <tr>
    <td><div id="TBody">2</div></td>
    <td><div id="TBody">Test results are correct and discrepancies explained </div></td>
    <td><div id="TBody">Software Verification Results</div></td> 
    <td><div id="TBody">Sprint review of unit tests and functional tests</div></td>
  </tr>  

  <tr>
    <td><div id="TBody">3</div></td>
    <td><div id="TBody">Test coverage of high level requirements is achieved</div></td> 
    <td><div id="TBody">Software Verification Results</div></td>    
    <td><div id="TBody">Sprint review of unit tests and functional tests</div></td>
  </tr> 

  <tr>
    <td><div id="TBody">4</div></td>
    <td><div id="TBody">Test coverage of low level requirements is achieved</div></td> 
    <td><div id="TBody">Software Verification Results</div></td>
    <td><div id="TBody">Sprint review of unit tests and functional tests</div></td>
  </tr> 

  <tr>
    <td><div id="TBody">5</div></td>
    <td><div id="TBody">Test coverage of software structure (modified condition / decision coverage) is achieved</div></td> 
    <td><div id="TBody">Software Verification Results</div></td>
    <td><div id="TBody">No difference</div></td>
  </tr>

  <tr>
    <td><div id="TBody">6</div></td>
    <td><div id="TBody">Test coverage of software structure (decision coverage) is achieved</div></td> 
    <td><div id="TBody">Software Verification Results</div></td>
    <td><div id="TBody">No difference</div></td>
  </tr>

  <tr>
    <td><div id="TBody">7</div></td>
    <td><div id="TBody">Test coverage of software structure (statement coverage) is achieved</div></td> 
    <td><div id="TBody">Software Verification Results</div></td>
    <td><div id="TBody">No difference</div></td>
  </tr>

  <tr>
    <td><div id="TBody">8</div></td>
    <td><div id="TBody">Test coverage of software structure (data coupling and control coupling) is achieved</div></td> 
    <td><div id="TBody">Software Verification Results</div></td>
    <td><div id="TBody">No difference</div></td>
  </tr>

  <tr>
    <td><div id="TBody">9</div></td>
    <td><div id="TBody">Verification of additional code, that cannot be traced to Source Code, is achieved.</div></td> 
    <td><div id="TBody">Software Verification Results</div></td>
    <td><div id="TBody">No difference</div></td>
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
    <td><div id="TBody">No difference</div></td>
  </tr>

  <tr>
    <td><div id="TBody">2</div></td>
    <td><div id="TBody">Baselines and traceability are established</div></td>
    <td><div id="TBody">Software Configuration index <br/><br/>
                        SCM Records</div></td> 
    <td><div id="TBody">Baseline generated by cloning the CI / CD, traceability checked not as normal with documented traceability matrixes, but by verifying traceability between annotated unit tests, functional tests and user stories.</div></td>
  </tr>  

  <tr>
    <td><div id="TBody">3</div></td>
    <td><div id="TBody">Problem reporting, change control, change review, and configuration status accounting are established</div></td> 
    <td><div id="TBody">Problem reports<br/><br/>
                        SCM Records</div></td>    
    <td><div id="TBody">No difference</div></td>
  </tr> 

  <tr>
    <td><div id="TBody">4</div></td>
    <td><div id="TBody">Archive, retrieval, and release are established</div></td> 
    <td><div id="TBody">SCM Records</div></td>
    <td><div id="TBody">No difference</div></td>
  </tr> 

  <tr>
    <td><div id="TBody">5</div></td>
    <td><div id="TBody">Software load control is established</div></td> 
    <td><div id="TBody">SCM Records</div></td>
    <td><div id="TBody">No difference</div></td>
  </tr>

  <tr>
    <td><div id="TBody">6</div></td>
    <td><div id="TBody">Software life cycle environment control is established</div></td> 
    <td><div id="TBody">Software Life Cycle Environment Configuration Index<br/><br/>
                        SCM Records</div></td>
    <td><div id="TBody">No difference</div></td>
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
    <td><div id="TBody">Assurance is obtained that software plans and standards are developed and reviewed for compliance with this document and for consistency.</div></td>
    <td><div id="TBody">Software Quality Assurance Records</div></td> 
    <td><div id="TBody">No difference</div></td>
  </tr>

  <tr>
    <td><div id="TBody">2</div></td>
    <td><div id="TBody">Assurance is obtained that software life cycle processes comply with approved software plans.</div></td>
    <td><div id="TBody">Software Quality Assurance Records</div></td> 
    <td><div id="TBody">No difference</div></td>
  </tr>  

  <tr>
    <td><div id="TBody">3</div></td>
    <td><div id="TBody">Assurance is obtained that software life cycle processes comply with approved software standards.</div></td> 
    <td><div id="TBody">Software Quality Assurance Records</div></td>    
    <td><div id="TBody">No difference</div></td>
  </tr> 

  <tr>
    <td><div id="TBody">4</div></td>
    <td><div id="TBody">Assurance is obtained that transition criteria for the software life cycle processes are satisfied.</div></td> 
    <td><div id="TBody">Software Quality Assurance Records</div></td>    
    <td><div id="TBody">No difference</div></td>
  </tr> 
 
  <tr>
    <td><div id="TBody">5</div></td>
    <td><div id="TBody">Assurance is obtained that software conformity review is conducted.</div></td> 
    <td><div id="TBody">Software Quality Assurance Records</div></td>    
    <td><div id="TBody">No difference</div></td>
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
    <td><div id="TBody">No difference</div></td>
  </tr>

  <tr>
    <td><div id="TBody">2</div></td>
    <td><div id="TBody">The means of compliance is proposed and agreement with the Plan for Software Aspects of Certification is obtained</div></td>
    <td><div id="TBody">Plan for software aspects of certification</div></td> 
    <td><div id="TBody">No difference</div></td>
  </tr>  

  <tr>
    <td><div id="TBody">3</div></td>
    <td><div id="TBody">Compliance substantiation is provided</div></td> 
    <td><div id="TBody">Software Accomplishment Summary<br/><br/>
                        Software Configuration Index</div></td>    
    <td><div id="TBody">No difference</div></td>
  </tr> 
</table>
<br/>

So there you have it, a proposal on what a more agile DO-178 development process might look like. I want to make it clear, none of this was developed in a vacuum or my own work, but cherry picked from various sources, which I'll attribute to as part of the literature study of my thesis. 

The question now is, will this pass certification, and can this agile process deliver software of at least the same robustness / quality as a waterfall process delivers. For this question, I will be guiding two three-man student groups to complete the same software project, one group following the waterfall model and another group following the agile model. More on that in the next post (experimental design).

A lot of this post has been quite abstract, not mentioning any specific software solutions to be used during development. The next post will detail the exact solutions the students will use in the form of PSAC and SDP documents, giving more clarity of an agile DO-178 development process. 

If I have missed anything or you would like to make a suggestion, kindly do so at the discussion on [HN](https://news.ycombinator.com/item?id=8937549) and [reddit](http://www.reddit.com/r/programming/comments/2tg71e/do178b_crash_course/). Comments and suggestions are very welcome.

If you are currently; or in the past have worked on DO-178 projects, it would be appreciated if you would be so kind as to [take part in a quick survey](https://www.surveymonkey.com/s/SV9KX7M) about the state of DO-178 development. I will release the results of this survey shortly. Thank you for everyone who has completed the survey already.