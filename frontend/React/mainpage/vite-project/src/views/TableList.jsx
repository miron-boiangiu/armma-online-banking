import React from "react";
import * as Components from "../layouts/Components";

// react-bootstrap components
import {
  Card,
  Table,
  Container,
  Row,
  Col,
} from "react-bootstrap";

function TableList() {
  return (
    <>
      <Container fluid>
        <Row>
          <Col md="12">
            <Card className="strpied-tabled-with-hover">
              <Card.Header>
                <Card.Title><Components.H4Text>My Transactions</Components.H4Text></Card.Title>
                {/* <p className="card-category">
                  Here is a subtitle for this table
                </p> */}
              </Card.Header>
              <Card.Body className="table-full-width table-responsive px-0">
                <Table className="table-hover table-striped">
                  <thead>
                    <tr>
                      <th className="border-0">ID</th>
                      <th className="border-0">From</th>
                      <th className="border-0">To</th>
                      <th className="border-0">Ammount</th>
                      <th className="border-0">Date</th>
                    </tr>
                  </thead>
                  <tbody>
                  <tr>
                      <td>TODO</td>
                      <td><span style={{fontSize: '10px'}}>Sa apara nume cont in loc de iban daca e contul personal</span></td>
                      
                    </tr>
                    <tr>
                      <td>1</td>
                      <td>RO87PORL4698371774138395</td>
                      <td>RO96RZBR6556328875496675</td>
                      <td>1100</td>
                      <td>13-05-2024</td>
                    </tr>
                    <tr>
                      <td>2</td>
                      <td>RO15PORL6161978552128721</td>
                      <td>RO71PORL5367462556175634</td>
                      <td>20</td>
                      <td>13-05-2024</td>
                    </tr>
                    <tr>
                      <td>3</td>
                      <td>RO16RZBR7184943724655425</td>
                      <td>RO96RZBR9494582282544166</td>
                      <td>5042</td>
                      <td>13-05-2024</td>
                    </tr>
                    <tr>
                      <td>4</td>
                      <td>RO12PORL4723364825388489</td>
                      <td>RO67PORL4563759184254749</td>
                      <td>532</td>
                      <td>13-05-2024</td>
                    </tr>
                    <tr>
                      <td>5</td>
                      <td>RO59PORL5993184648321656</td>
                      <td>RO79RZBR4723245378378862  </td>
                      <td>54633</td>
                      <td>13-05-2024</td>
                    </tr>
                    <tr>
                      <td>6</td>
                      <td>RO77RZBR1431684131614975</td>
                      <td>RO35PORL5616451688283735</td>
                      <td>123</td>
                      <td>13-05-2024</td>
                    </tr>
                  </tbody>
                </Table>
              </Card.Body>
            </Card>
          </Col>
        </Row>
      </Container>
    </>
  );
}

export default TableList;
