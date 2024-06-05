# project_quotes

### Overview
This project aims to work with a dataset of historical projects collected from an architectural firm. The dataset focuses on hours quoted by directors of the firm, and overtime hours worked for that project. The projects (observations) are mostly residential renovation or home extension projects across London. The hours are recorded against different Stages set out by RIBA(Royal Institute of British Architects).

The goal is to identify patterns and provide insights to improve the accuracy of future project quotations.

This project was inspired by my first-hand experience as an architect, where I observed a recurring challenge in the industry with project management and quoting accuracy. It is no doubt that accurate project quoting is crucial for both client satisfaction and efficient resource and time management. I saw this opportunity to leverage my data-driven skills to provide valuable insights, by understanding the patterns and discrepancies in quoted versus actual hours. I aim to use this project to help this architectural firm streamline their quoting process, ensuring more precise estimates and better project planning in the future.

For data protection, the site address and director entries have been modified and anonymized in the notebooks.

### Data Dictionary
| Variable          | Definition                                           |
|-------------------|------------------------------------------------------|
| Project No        | Project number on file                               |
| Project Address   | Project address                                      |
| Postcode          | Project postcode                                     |
| Director          | Director in charge                                   |
| Stage 1           | Hours quoted for Stage 1 (Preparation and Briefing)  |
| Stage 2           | Hours quoted for Stage 2 (Concept Design)            |
| Stage 3           | Hours quoted for Stage 3 (Spatial Coordination)      |
| Stage 4           | Hours quoted for Stage 4 (Technical Design)          |
| Stage 1 OT        | Overtime hours worked during Stage 1                 |
| Stage 2 OT        | Overtime hours worked during Stage 2                 |
| Stage 3 OT	    | Overtime hours worked during Stage 3                 |
| Stage 4 OT	    | Overtime hours worked during Stage 4                 |
| Current Est Value | Current estimated property value as of June 2024     |

### Variable Notes
The main body of the dataset includes numerical entries of hours spent on different RIBA stages 1 through 4. For further reading, refer to: [RIBA Stages](https://www.architecture.com/knowledge-and-resources/resources-landing-page/riba-plan-of-work)

Current estimated property value resource: [Property Checker](https://propertychecker.co.uk/)