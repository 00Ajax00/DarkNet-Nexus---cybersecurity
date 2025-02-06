import { renderHook, act } from "@testing-library/react";
import useAuth from "../hooks/useAuth";

test("should handle login correctly", async () => {
  const { result } = renderHook(() => useAuth());

  act(() => {
    result.current.login({ username: "test", password: "password" });
  });

  expect(localStorage.getItem("token")).toBeTruthy();
});
