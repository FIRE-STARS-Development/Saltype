import _ from "lodash";
import { setLocale, type LocaleObject } from "yup";
import { suggestive } from "yup-locale-ja";

export default defineNuxtPlugin(() => {
    const customeLocaleObject: LocaleObject = {
        mixed: {
            required: ({ label }) => "※" + (label ? label + "は" : "") + "必須項目です",
        }
    }

    const LocaleObject = _.merge({}, suggestive, customeLocaleObject);

    setLocale(LocaleObject);
})