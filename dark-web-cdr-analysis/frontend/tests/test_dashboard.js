import { render, screen } from "@testing-library/react";
import Dashboard from "../pages/index";

test("renders dashboard page", () => {
  render(<Dashboard />);
  expect(screen.getByText(/Dashboard/i)).toBeInTheDocument();
});
