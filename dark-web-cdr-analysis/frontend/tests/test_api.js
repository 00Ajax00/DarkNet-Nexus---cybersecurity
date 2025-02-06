import { renderHook } from "@testing-library/react";
import useFetch from "../hooks/useFetch";

test("fetches data from API", async () => {
  global.fetch = jest.fn(() =>
    Promise.resolve({
      json: () => Promise.resolve({ data: "test data" }),
    })
  );

  const { result } = renderHook(() => useFetch("/api/test"));
  expect(result.current.data).toEqual(null);
});
