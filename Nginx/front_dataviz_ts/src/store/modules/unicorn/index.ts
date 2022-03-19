import { Module } from "vuex";
import { IState } from "./interfaces";
import { getters } from "./getters";
import { actions } from "./actions";
import { mutations } from "./mutations";
import { state } from "./state";

// Module
const auth: Module<IState, IState> = {
    state,
    getters,
    mutations,
    actions
};

export default auth;