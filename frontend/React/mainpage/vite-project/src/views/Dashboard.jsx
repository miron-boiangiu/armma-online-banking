import React from "react";
import 'chartist/dist/chartist.min.css'; 
import * as Components from "../layouts/Components";
import 'bootstrap/dist/css/bootstrap.min.css';
import Account from '../views/Account'
import {
  Container,
  Row,
  Col,
  Form,
  Modal,
} from "react-bootstrap";

export default function Dashboard() {
  const [showModal, setShowModal] = React.useState(false);
  return (
    <>
      <Container fluid>
        <Row>
          <Col xs="12">
          <Components.Button onClick={() => setShowModal(true)} style={{marginBottom: '20px', backgroundColor : '#314b5e', borderColor: '#314b5e'}}>Add account</Components.Button>
          </Col>
          <Account />
          <Account />
          <Account />
          <Account />
          <Account />
          <Account />
        </Row>
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
                  <label>Account name</label>
                  <Form.Control
                    placeholder="Account name"
                    type="text"
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
      </Container>
    </>
  );
}


