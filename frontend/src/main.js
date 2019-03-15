import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueSession from 'vue-session'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import VueCookie from 'vue-cookie';
import * as Sentry from '@sentry/browser'
import VueAnalytics from 'vue-analytics'

Vue.config.productionTip = false;

Vue.use(VueSession);

Vue.use(Vuetify, {iconfont: 'md'});

Vue.use(VueCookie);

if (process.env.NODE_ENV === 'production') {
    Sentry.init({
        dsn: process.env.VUE_APP_SENTRY_PUBLIC_DSN,
        integrations: [new Sentry.Integrations.Vue({Vue})]
    });

    Vue.use(VueAnalytics, {
        id: process.env.VUE_APP_GOOGLE_ANALYTICS,
        router
    });
}

let vm = new Vue({
    router,
    render: h => h(App)
}).$mount('#app');

export default vm;
