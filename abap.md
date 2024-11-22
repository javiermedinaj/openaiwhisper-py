ABAP (Advanced Business Application Programming) is a fourth generation language, owned by SAP, used to program most of its products (R/3, mySAP Business suite...). It uses Open SQL statements to connect to virtually any database. It has thousands of functions for handling files, databases, dates, etc. It allows RFC (Remote Function Calls) connections to connect SAP systems with any other system or programming language.

SAP supplies a limited installation of R/3 called MiniSAP for practicing ABAP programming. MiniSap has been replaced by SAP NetWeaver 7.03 Trial Version

History
ABAP was developed by SAP as a reporting language for SAP R/2, in the 1980s, a platform that allowed large corporations to build business applications for materials and finance management. ABAP, very similar to COBOL in its origins, originally stood for Allgemeiner Berichtsaufbereitungsprozessor, German words for generic processor for the preparation of reports. In its beginnings ABAP included the concept of Logical Databases, which provided a high level of abstraction for accessing databases.

ABAP was intended as a programming language for end users to manipulate information, but 4GL became too complicated for normal users, so experienced programmers were needed to carry out developments.

ABAP remained the development language for the next client-server version of SAP R/3, which was released in 1992, in which almost the entire system, except for the basic system calls, were written in ABAP. In 1999, with the release of version 4.6 of R/3, SAP released an object-oriented extension called ABAP Objects. The most current version at this time from SAP is release 6.6.

SAP's latest development platform, NetWeaver, supports ABAP and Java as programming languages.

Transactions
A transaction in SAP terminology is the execution of a program. The normal way to execute ABAP code in the SAP system is by entering a transaction code (for example, VA01 is the transaction code for “Create Sales Orders”). Transactions can be called through system-defined, user-specified, or role-based menus. They can also be invoked by entering the transaction code directly into the command field, which is present on all SAP screens. Transactions can also be invoked by code using the ABAP statements “CALL TRANSACTION” and “LEAVE TO TRANSACTION”. The term “transaction” should not be misinterpreted; in the context described here, a transaction simply means the calling of a program to execute. In other programming contexts, “transaction” often refers to an indivisible operation on data. This last concept also exists in SAP and is called LUW (Logical Unit of Work). In the course of a transaction (program execution), there can be different LUWs.

ABAP is a logical programming language on the SAP platform. It is recommended to install SAP ECC, in the three-tier mode, server-presentation-database. The ABAP academy is highly recommended for those who are passionate about SAP programming, since the above is only a small part of what the SAP system can cover.

Types of ABAP programs
As in other programming languages, an ABAP program is not simply an executable unit or a library, but provides executable code for other programs not executed independently.

ABAP distinguishes between two types of programs:

Reports
Module pool
Reports follow a relatively simple programming model, where the user enters a series of parameters and the program uses them to produce a report in the form of an interactive list. The term report can be misleading since reports can be designed to modify data, the reason these programs are called reports is the “list-oriented” output they produce.

Module pools define more complex patterns of user interaction across a collection of screens. The term “screen” refers to the actual, physical image that users can see. Each screen also has a “logic flow,” which refers to implicit ABAP code invoked by the screens. Each screen has its own logic flow, which is divided into “PBO” (Process Before Output) and PAI (Process after Input). In SAP documentation the term “dynpro” (dynamic program) refers to the combination of screens and logic flow.

The types of non-executable programs are:

INCLUDE modules
Subroutine pools
Function groups
Object classes
Interfaces
Type pools