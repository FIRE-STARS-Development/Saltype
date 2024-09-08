<script setup lang="ts">
import { ErrorMessage, Field } from "vee-validate";
import Text from "~/components/atoms/texts/Text.vue";

interface Props {
  modelValue: string;
  name: string;
}

const props = defineProps<Props>();
const emit = defineEmits(['update:modelValue']);

const updateValue = (value: string) => {
  emit('update:modelValue', value);
};
</script>

<template>
  <div>
    <Field :name="props.name" :value="props.modelValue" @update:modelValue="updateValue" v-slot="{ field }">
      <slot name="label"></slot>
      <slot name="input" :field="field"></slot>
    </Field>
    <ErrorMessage :name="props.name" v-slot="{ message }">
      <Text color="blue" :text="message" />
    </ErrorMessage>
  </div>
</template>
