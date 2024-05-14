import React from "react";
import * as Components from "../layouts/Components";

// react-bootstrap components
import {
  Card,
  Form,
  Container,
  Row,
  Col
} from "react-bootstrap";

function User() {
  return (
    <>
      <Container fluid>
        <Row>
          <Col md="12">
            <Card>
              <Card.Header>
                {/* <Card.Title as="h3" style={{textAlign : 'center'}}>Details</Card.Title> */}
                
              </Card.Header>
              <Card.Body>
                <Card.Subtitle as = "h3">From</Card.Subtitle>
                <Form>
                  <Row>
                    <Col className="pr-1" md="12">
                      <Form.Group>
                        <label>IBAN</label>
                        <Form.Control
                          // defaultValue="Creative Code Inc."
                          placeholder="IBAN"
                          type="text"
                        ></Form.Control>
                      </Form.Group>
                    </Col>
                    
                  </Row>
                  
                  <Row>
                  <Card.Subtitle as = "h3" style={{margin: '15px 0px 0px 15px'}}>To</Card.Subtitle>
                  </Row>
                  <Row>
                    <Col className="pr-1" md="12">
                      <Form.Group>
                        <label>IBAN</label>
                        <Form.Control
                          // defaultValue="Creative Code Inc."
                          placeholder="IBAN"
                          type="text"
                        ></Form.Control>
                      </Form.Group>
                    </Col>
                    
                  </Row>
                  <Row>
                    <Col className="pr-1" md="6">
                      <Form.Group>
                        <label>Name</label>
                        <Form.Control
                          // defaultValue="Creative Code Inc."
                          placeholder="Name"
                          type="text"
                        ></Form.Control>
                      </Form.Group>
                    </Col>
                    
                  </Row>
                  <Row>
                    <Col className="pr-1" md="4">
                      <Form.Group>
                        <label>Amount</label>
                        <Form.Control
                          // defaultValue="Creative Code Inc."
                          placeholder="Value"
                          type="number"
                        ></Form.Control>
                      </Form.Group>
                    </Col>
                    
                  </Row>
                  
                  <Row>
                    <Col md="12">
                      <Form.Group>
                        <label>Description</label>
                        <Form.Control
                          cols="80"
                          placeholder="Description"
                          rows="4"
                          as="textarea"
                        ></Form.Control>
                      </Form.Group>
                    </Col>
                  </Row>
                  <Components.Button
                    className="btn-fill pull-right"
                    type="submit"
                    variant="info"
                    style={{marginTop : '10px'}}
                  >
                    Send
                  </Components.Button>
                  <div className="clearfix"></div>
                </Form>
              </Card.Body>
            </Card>
          </Col>
          
        </Row>
      </Container>
    </>
  );
}

export default User;
