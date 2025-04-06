import { createHashRouter, Navigate, RouterProvider } from "react-router-dom";
import AppLayout from "./Components/AppLayout";

function RoutesHandler() {
  const router = createHashRouter([
    {
      path: "/",
      element: <AppLayout />,
      children: [
        // {
        //   path: "/",
        //   element: <Home />,
        // },
      ],
    },
  ]);
  return <RouterProvider router={router} />;
}

export default RoutesHandler;
