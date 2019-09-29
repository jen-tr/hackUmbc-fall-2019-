import { Component, OnInit, SystemJsNgModuleLoader } from '@angular/core';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  url;
  name = new FormControl('');
  constructor() { }

  ngOnInit() {
  }

  updateName() {
    console.log("this.name: " + this.name.value);
    //this.name.setValue('Nancy');
  }


  onSelectFile(event) { // called each time file input changes
    if (event.target.files && event.target.files[0]) {
      var reader = new FileReader();

      reader.readAsDataURL(event.target.files[0]); // read file as data url

      reader.onload = (event) => { // called once readAsDataURL is completed
        this.url = event.target.result;
      }
    }

    console.log('' + this.url.value);


}

}
