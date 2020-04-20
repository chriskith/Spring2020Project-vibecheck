import { UPDATE_PROFILE } from "./types";

export const updateProfile = (profile) => (dispatch) => {
  fetch(`/api/profiles/${profile.id}/`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(profile),
  })
    .then((response) => {
      return response.json();
    })
    .then((profile) => {
      console.log(profile);
      dispatch({
        type: UPDATE_PROFILE,
        payload: profile,
      });
    })
    .catch((err) => console.log(err));
};
