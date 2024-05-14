import React from "react";
import 'chartist/dist/chartist.min.css'; 
import * as Components from "../layouts/Components";
import 'bootstrap/dist/css/bootstrap.min.css';
import { useState, useEffect } from "react";
import axios from "axios";

import {
  Card,
  Nav,
  Row,
  Col,
  Modal,
  Dropdown,
  Form,
  Button
} from "react-bootstrap";
import { API_USER_INFO_URL } from "api_routes";

export default function Account() {
  const [showModal, setShowModal] = React.useState(false);

    return (
        <Col lg="4" sm="6">
            <Card className="card-stats">
              <Card.Body style={{position : 'relative'}}>
                <Row>
                  <Col xs="6">
                  <div className="numbers">
                      <p className="card-category" style={{ textAlign: 'center' }}>Account Name</p>
                      <Card.Title as="h4" style={{ textAlign: 'center' }}>Card BT</Card.Title>
                    </div>
                  </Col>
                  <Col xs="4">
                    <div className="numbers">
                      <p className="card-category" style={{ textAlign: 'center' }}>Money</p>
                      <Card.Title as="h4" style={{ textAlign: 'center' }}>1150</Card.Title>
                    </div>
                  </Col>
                  <Col xs = "2">
                    <Dropdown>
                      <Dropdown.Toggle
                        as={Nav.Link}
                        style={{
                        color : '#074168',         
                        zIndex: 1000,
                        marginLeft : 0,
                        left : '0px',
                        width : '20px'
                        
                      }}
                      >
                        <i style={{color : '#074168',
                         textAlign : 'left',
                          position: 'absolute',   
                         right: '0px',            
                         left: '0px',}}
                        className="bi bi-gear-fill" ></i>
                      </Dropdown.Toggle>
                      <Dropdown.Menu>
                        <Dropdown.Item
                          href="test"
                          onClick={(e) => e.preventDefault()}
                          
                        >
                          Close Account
                        </Dropdown.Item>
                        
                      </Dropdown.Menu>
                    </Dropdown>
                  </Col>
                    
                </Row>
                
                <Row>
                  <Col xs="12">
                  <div className="numbers">
                      <p className="card-category" style={{ textAlign: 'center' }}>IBAN</p>
                      <Card.Title as="h4" style={{ textAlign: 'center' }}>RO45PORL4916331719145161</Card.Title>
                    </div>
                  </Col>
                </Row>
              </Card.Body>
                <hr></hr>
                <Row>
                  <Col xs="6">
                  <div className="numbers">
                  <Components.Button onClick={() => setShowModal(true)} style={{padding: '12px 20px', backgroundColor : '#314b5e', marginLeft : '30px'}} > Add money</Components.Button>
                    </div>
                  </Col>
                  <Col xs="4">
                    <div className="numbers">
                    <Components.GhostButton style={{padding: '12px 20px', marginLeft : '20px', marginBottom : '20px', borderColor: '#314b5e'}}><span style={{color : '#314b5e'}}>Transfer</span></Components.GhostButton>

                    </div>
                  </Col>
                  <Modal
                      className="modal-large"
                      show={showModal} 
                      onHide={() => setShowModal(false)}
                      style={{width: '400px', 
                      maxWidth: '100%',  
                      margin: '1.75rem auto',
                      marginLeft : '40%'
                    }}
                  >
                      
                    <Modal.Body className="text-center" style={{width : '100%'}}>
                      <Form style={{width : '100%'}} id="moneyForm">
                        <Row>
                          <Col className="pr-1" md="12">
                            <Form.Group>
                              <label>Insert money amount</label>
                              <Form.Control
                                placeholder="Money"
                                type="number"
                              ></Form.Control>
                            </Form.Group>
                          </Col>
                        </Row>
                      </Form>
                      </Modal.Body>
                      <div className="modal-footer">
                          <Components.GhostButton
                              className="btn-simple"
                              type="button"
                              variant="link"
                              onClick={() => setShowModal(false)}
                          >
                              Back
                          </Components.GhostButton>
                          <Components.Button
                          className="btn-fill pull-right"
                          type="submit"
                          variant="info"
                          form="moneyForm"
                        >
                          Confirm
                        </Components.Button>
                      </div>
                  </Modal>
                  
                </Row>
                
            </Card>
          </Col>
    )
}