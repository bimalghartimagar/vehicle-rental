import { shallowMount } from "@vue/test-utils";
import Splash from "@/components/Splash.vue";

describe("Splash.vue", () => {
  it("renders props.msg when passed", () => {
    const msg = "new message";
    const wrapper = shallowMount(Splash, {
      propsData: { msg }
    });
    expect(wrapper.text()).toMatch(msg);
  });
});
