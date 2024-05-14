
import Dashboard from './views/Dashboard.jsx'
import UserProfile from "./views/UserProfile.jsx";
import TableList from "./views/TableList.jsx";
import 'bootstrap/dist/css/bootstrap.min.css';
import Transfer from "./views/Transfer.jsx"

const dashboardRoutes = [
  {
    path: "/dashboard",
    name: "My accounts",
    icon: "bi bi-coin",
    component: Dashboard,
    layout: "/admin"
  },
  {
    path: "/user",
    name: "Profile",
    icon: "bi bi-person-fill",
    component: UserProfile,
    layout: "/admin"
  },
  {
    path: "/transfer",
    name: "Transfer money",
    icon: "bi bi-arrow-left-right",
    component: Transfer,
    layout: "/admin"
  },
  {
    path: "/transactions",
    name: "Transactions",
    icon: "bi bi-clock-history",
    component: TableList,
    layout: "/admin"
  }
];

export default dashboardRoutes;
