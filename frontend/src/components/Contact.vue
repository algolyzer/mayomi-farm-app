<template>
  <div class="contact">
    <!-- Hero Section -->
    <section class="gradient-bg text-white py-20">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h1 class="text-4xl md:text-5xl font-bold mb-6 font-bengali">যোগাযোগ করুন</h1>
        <p class="text-xl text-green-100 font-bengali max-w-3xl mx-auto">
          আমরা আপনার সেবায় সর্বদা প্রস্তুত
        </p>
      </div>
    </section>

    <!-- Contact Section -->
    <section class="py-20 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
          <!-- Contact Information -->
          <div>
            <h2 class="text-3xl font-bold mb-8 font-bengali text-gray-800">যোগাযোগের তথ্য</h2>
            
            <div class="space-y-6">
              <!-- Phone -->
              <div class="flex items-start gap-4 p-6 bg-gray-50 rounded-xl hover:shadow-lg transition-shadow">
                <div class="text-3xl">📞</div>
                <div>
                  <h3 class="text-xl font-bold mb-2 font-bengali text-gray-800">ফোন</h3>
                  <a href="tel:+8801711727357" class="text-primary-600 hover:text-primary-700 text-lg">
                    +8801711727357
                  </a>
                  <p class="text-gray-600 text-sm font-bengali mt-1">সকাল ৮টা থেকে রাত ৮টা</p>
                </div>
              </div>

              <!-- Email -->
              <div class="flex items-start gap-4 p-6 bg-gray-50 rounded-xl hover:shadow-lg transition-shadow">
                <div class="text-3xl">📧</div>
                <div>
                  <h3 class="text-xl font-bold mb-2 font-bengali text-gray-800">ইমেইল</h3>
                  <a href="mailto:nishat@manishatagro.com" class="text-primary-600 hover:text-primary-700 text-lg">
                    nishat@manishatagro.com
                  </a>
                  <p class="text-gray-600 text-sm font-bengali mt-1">২৪ ঘন্টার মধ্যে উত্তর দিব</p>
                </div>
              </div>

              <!-- Location -->
              <div class="flex items-start gap-4 p-6 bg-gray-50 rounded-xl hover:shadow-lg transition-shadow">
                <div class="text-3xl">📍</div>
                <div>
                  <h3 class="text-xl font-bold mb-2 font-bengali text-gray-800">ঠিকানা</h3>
                  <p class="text-gray-700 text-lg">Vabakhali bazar</p>
                  <p class="text-gray-600 text-sm font-bengali mt-1">সরাসরি পরিদর্শনের জন্য আগে যোগাযোগ করুন</p>
                </div>
              </div>
            </div>

            <!-- Social Media / Additional Info -->
            <div class="mt-8 p-6 gradient-bg text-white rounded-xl">
              <h3 class="text-xl font-bold mb-4 font-bengali">কাজের সময়</h3>
              <ul class="space-y-2 text-green-100 font-bengali">
                <li class="flex justify-between">
                  <span>রবিবার - বৃহস্পতিবার:</span>
                  <span>৮:০০ - ২০:০০</span>
                </li>
                <li class="flex justify-between">
                  <span>শুক্রবার:</span>
                  <span>৮:০০ - ১২:০০, ১৪:০০ - ২০:০০</span>
                </li>
                <li class="flex justify-between">
                  <span>শনিবার:</span>
                  <span>৮:০০ - ২০:০০</span>
                </li>
              </ul>
            </div>
          </div>

          <!-- Contact Form -->
          <div>
            <h2 class="text-3xl font-bold mb-8 font-bengali text-gray-800">বার্তা পাঠান</h2>
            
            <!-- Success Message -->
            <div v-if="showSuccess" class="mb-6 p-4 bg-green-100 border border-green-400 text-green-700 rounded-lg font-bengali">
              ✅ আপনার বার্তা সফলভাবে পাঠানো হয়েছে। আমরা শীঘ্রই আপনার সাথে যোগাযোগ করব।
            </div>

            <!-- Error Message -->
            <div v-if="showError" class="mb-6 p-4 bg-red-100 border border-red-400 text-red-700 rounded-lg font-bengali">
              ❌ দুঃখিত, একটি সমস্যা হয়েছে। অনুগ্রহ করে আবার চেষ্টা করুন।
            </div>

            <form @submit.prevent="submitForm" class="space-y-6">
              <!-- Name -->
              <div>
                <label class="block text-gray-700 font-semibold mb-2 font-bengali">নাম *</label>
                <input 
                  v-model="form.name"
                  type="text" 
                  required
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent font-bengali"
                  placeholder="আপনার নাম লিখুন"
                />
              </div>

              <!-- Email -->
              <div>
                <label class="block text-gray-700 font-semibold mb-2 font-bengali">ইমেইল *</label>
                <input 
                  v-model="form.email"
                  type="email" 
                  required
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                  placeholder="your@email.com"
                />
              </div>

              <!-- Phone -->
              <div>
                <label class="block text-gray-700 font-semibold mb-2 font-bengali">ফোন নম্বর *</label>
                <input 
                  v-model="form.phone"
                  type="tel" 
                  required
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                  placeholder="+880 1711 727357"
                />
              </div>

              <!-- Message -->
              <div>
                <label class="block text-gray-700 font-semibold mb-2 font-bengali">বার্তা *</label>
                <textarea 
                  v-model="form.message"
                  required
                  rows="5"
                  class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent font-bengali resize-none"
                  placeholder="আপনার বার্তা লিখুন..."
                ></textarea>
              </div>

              <!-- Submit Button -->
              <button 
                type="submit"
                :disabled="loading"
                class="w-full btn-primary flex items-center justify-center gap-2"
                :class="{ 'opacity-50 cursor-not-allowed': loading }"
              >
                <span v-if="!loading" class="font-bengali">বার্তা পাঠান</span>
                <span v-else class="font-bengali">পাঠানো হচ্ছে...</span>
                <span v-if="!loading">📤</span>
              </button>
            </form>
          </div>
        </div>

        <!-- Map Section -->
        <div class="mt-20">
          <h2 class="text-3xl font-bold mb-8 text-center font-bengali text-gray-800">আমাদের অবস্থান</h2>
          <div class="card overflow-hidden">
            <div class="bg-gray-200 h-96 flex items-center justify-center">
              <div class="text-center">
                <div class="text-6xl mb-4">📍</div>
                <p class="text-gray-600 font-bengali text-lg">Vabakhali bazar</p>
                <p class="text-gray-500 text-sm font-bengali mt-2">মানচিত্র শীঘ্রই যুক্ত করা হবে</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Quick Contact CTA -->
        <div class="mt-20 gradient-bg text-white rounded-3xl p-12 text-center">
          <h2 class="text-3xl md:text-4xl font-bold mb-6 font-bengali">
            এখনই যোগাযোগ করুন
          </h2>
          <p class="text-xl mb-8 text-green-100 font-bengali">
            মানসম্মত ও নিরাপদ কৃষিপণ্যের জন্য আজই অর্ডার করুন
          </p>
          <div class="flex flex-wrap justify-center gap-4">
            <a 
              href="tel:+8801711727357" 
              class="bg-white text-primary-600 px-8 py-4 rounded-lg font-semibold hover:bg-gray-100 transition-all duration-300 shadow-xl hover:shadow-2xl font-bengali inline-flex items-center gap-2"
            >
              <span>📞</span>
              <span>কল করুন</span>
            </a>
            <a 
              href="https://wa.me/8801711727357" 
              target="_blank"
              class="bg-green-600 text-white px-8 py-4 rounded-lg font-semibold hover:bg-green-700 transition-all duration-300 shadow-xl hover:shadow-2xl font-bengali inline-flex items-center gap-2"
            >
              <span>💬</span>
              <span>হোয়াটসঅ্যাপ</span>
            </a>
            <a 
              href="mailto:nishat@manishatagro.com"
              class="bg-primary-800 text-white px-8 py-4 rounded-lg font-semibold hover:bg-primary-900 transition-all duration-300 shadow-xl hover:shadow-2xl font-bengali inline-flex items-center gap-2"
            >
              <span>📧</span>
              <span>ইমেইল</span>
            </a>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Contact',
  data() {
    return {
      form: {
        name: '',
        email: '',
        phone: '',
        message: ''
      },
      loading: false,
      showSuccess: false,
      showError: false
    }
  },
  methods: {
    async submitForm() {
      this.loading = true
      this.showSuccess = false
      this.showError = false

      try {
        await axios.post('/api/contact', this.form)
        this.showSuccess = true
        
        // Reset form
        this.form = {
          name: '',
          email: '',
          phone: '',
          message: ''
        }

        // Hide success message after 5 seconds
        setTimeout(() => {
          this.showSuccess = false
        }, 5000)
      } catch (error) {
        console.error('Error submitting form:', error)
        this.showError = true

        // Hide error message after 5 seconds
        setTimeout(() => {
          this.showError = false
        }, 5000)
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style scoped>
</style>
