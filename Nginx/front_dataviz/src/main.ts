import {createApp} from 'vue'
import App from './app.vue'
import router from './router';
import store from './store';
import axios from 'axios';
import VueAxios from 'vue-axios';
import Toast, { POSITION } from "vue-toastification";
import "vue-toastification/dist/index.css";
import './assets/scss/tailwind.scss';

import {Store} from 'vuex';
import {IState} from './store/modules/unicorn/interfaces';

const app = createApp(App)
    .use(store)
    .use(router)
    .use(VueAxios, axios)
    .use(Toast, { position: POSITION.BOTTOM_RIGHT })
app.mount("#app" );

declare module '@vue/runtime-core' {
  interface ComponentCustomProperties  {
    $store: Store<IState>;
  }
}
