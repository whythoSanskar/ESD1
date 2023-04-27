import react, {useContext} from "react"
import {Navbar, Nav, Form, FormControl, Button, Badge} from 'react-bootstrap'
import {Link} from 'react-router-dom'
import { JobContext } from '../JobContext'

const NavBar =()=>{
    const [jobs, products] = useContext(JobContext)
    return(
        <Navbar bg="dark" expand="lg" variant="dark">
            <Navbar.Brand href="#home">Job Application System</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="mr-auto">            
                    <Badge className="mt-2" variant="primary">Number of person {jobs.data.length}</Badge>
                </Nav>
                {/* <Form onSubmit={ filterProduct } inline>
                        <Link to="/addproduct" className="btn btn-primary btn-sm mr-4">Add Product</Link>
                        <FormControl value = {search} onChange={updateSearch} type="text" placeholder="Search" className="mr-sm-2" />
                <Button type="submit"  variant="outline-primary">Search</Button>
                </Form> */}
            </Navbar.Collapse>
        </Navbar>
    );
}

export default NavBar;