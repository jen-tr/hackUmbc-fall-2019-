import { Component, OnInit, SystemJsNgModuleLoader } from '@angular/core';
import { FormControl } from '@angular/forms';


@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  url;
  imageVal = -1;
  budget = new FormControl('');
  

  constructor() { }

  ngOnInit() {
  }

  updateBudget() {
    console.log("this.budget: " + this.budget.value);
    //this.name.setValue('Nancy');
  }


  onSelectFile(event) { // called each time file input changes
    if (event.target.files && event.target.files[0]) {
      var reader = new FileReader();  

      reader.readAsDataURL(event.target.files[0]); // read file as data url

      reader.onload = (event) => { // called once readAsDataURL is completed
        let target: any = event.target; //<-- This (any) will tell compiler to shut up!
      let content: string = target.result;
        this.url = content;
      }
    }

    this.imageVal = Math.floor(Math.random() * Math.floor(5));

    console.log(this.imageVal.valueOf());

    //console.log('' + this.url.value);

}



}
